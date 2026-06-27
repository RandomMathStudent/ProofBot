from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List, Optional, Sequence, Tuple

from PIL import Image

from .config import PreprocessingConfig, StageConfig
from .models import (
    BaseStage,
    ImageLoader,
    PreprocessingResult,
    QualityEstimator,
    DocumentDetector,
    PerspectiveCorrector,
    OrientationDetector,
    LightingNormalizer,
    Denoiser,
    SuperResolver,
    ImageMetadata,
    QualityReport,
    PageDetection,
    StageContext,
    StageResult,
)
from .utils import extract_metadata, normalize_image_input
from .quality import BasicQualityEstimator
from .detection import BasicDocumentDetector
from .perspective import BasicPerspectiveCorrector
from .orientation import BasicOrientationDetector
from .lighting import BasicLightingNormalizer
from .denoise import BasicDenoiser
from .super_resolution import BasicSuperResolver


class DefaultImageLoader(ImageLoader):
    @property
    def name(self) -> str:
        return "default_image_loader"

    def load(self, image_input: Any) -> Tuple[Image.Image, ImageMetadata]:
        image = normalize_image_input(image_input)
        metadata = ImageMetadata(
            source=getattr(image_input, "filename", "input"),
            original_size=image.size,
            mode=image.mode,
            dpi=image.info.get("dpi") if hasattr(image, "info") else None,
            extra=extract_metadata(image, source=getattr(image_input, "filename", "input")),
        )
        return image, metadata


class PreprocessingPipeline:
    def __init__(
        self,
        config: PreprocessingConfig = PreprocessingConfig(),
        loader: Optional[ImageLoader] = None,
        quality_estimator: Optional[QualityEstimator] = None,
        document_detector: Optional[DocumentDetector] = None,
        perspective_corrector: Optional[PerspectiveCorrector] = None,
        orientation_detector: Optional[OrientationDetector] = None,
        lighting_normalizer: Optional[LightingNormalizer] = None,
        denoiser: Optional[Denoiser] = None,
        super_resolver: Optional[SuperResolver] = None,
        additional_stages: Optional[Sequence[BaseStage]] = None,
    ) -> None:
        self.config = config
        self.loader = loader or DefaultImageLoader()
        self.quality_estimator = quality_estimator or BasicQualityEstimator()
        self.document_detector = document_detector or BasicDocumentDetector()
        self.perspective_corrector = perspective_corrector or BasicPerspectiveCorrector()
        self.orientation_detector = orientation_detector or BasicOrientationDetector()
        self.lighting_normalizer = lighting_normalizer or BasicLightingNormalizer()
        self.denoiser = denoiser or BasicDenoiser()
        self.super_resolver = super_resolver or BasicSuperResolver()
        self.additional_stages = list(additional_stages or [])

    def process(self, image_input: Any) -> PreprocessingResult:
        image, metadata = self.loader.load(image_input)
        history: List[StageResult] = []

        quality = self._run_quality_assessment(image, metadata, history)
        pages = self._run_document_detection(image, history)

        page_image = self._apply_perspective_correction(image, pages, history)
        oriented_image = self._run_orientation_detection(page_image, history)
        normalized_image = self._run_lighting_normalization(oriented_image, history)
        denoised_image = self._run_optional_stage(
            normalized_image,
            self.config.denoise,
            self.denoiser.denoise,
            history,
            stage_name=self.denoiser.name,
        )
        super_resolved_image = self._run_optional_stage(
            denoised_image,
            self.config.super_resolution,
            self.super_resolver.upscale,
            history,
            stage_name=self.super_resolver.name,
        )
        final_image = self._run_additional_stages(super_resolved_image, history)

        return PreprocessingResult(
            image=final_image,
            metadata=metadata,
            quality=quality,
            pages=pages,
            history=history,
            config=asdict(self.config),
        )

    def _run_quality_assessment(
        self,
        image: Image.Image,
        metadata: ImageMetadata,
        history: List[StageResult],
    ) -> QualityReport:
        if not self.config.quality_assessment.enabled:
            history.append(StageResult(name="quality_assessment", status="skipped", details={}))
            return QualityReport(None, None, None, None, None, None)
        report = self.quality_estimator.estimate(image, metadata)
        history.append(StageResult(name=self.quality_estimator.name, status="completed", details={}))
        return report

    def _run_document_detection(self, image: Image.Image, history: List[StageResult]) -> List[PageDetection]:
        if not self.config.document_detection.enabled:
            history.append(StageResult(name="document_detection", status="skipped", details={}))
            return []
        pages, stage_result = self.document_detector.detect(image)
        history.append(stage_result)
        return pages

    def _apply_perspective_correction(
        self,
        image: Image.Image,
        pages: List[PageDetection],
        history: List[StageResult],
    ) -> Image.Image:
        if not self.config.perspective_correction.enabled or not pages:
            history.append(StageResult(name="perspective_correction", status="skipped", details={}))
            return image
        corrected_images: List[Image.Image] = []
        for page in pages[: self.config.page_limit] if self.config.page_limit else pages:
            corrected, stage_result = self.perspective_corrector.correct(image, page)
            corrected_images.append(corrected)
            history.append(stage_result)
        return corrected_images[0] if corrected_images else image

    def _run_orientation_detection(self, image: Image.Image, history: List[StageResult]) -> Image.Image:
        if not self.config.orientation_detection.enabled:
            history.append(StageResult(name="orientation_detection", status="skipped", details={}))
            return image
        corrected_image, stage_result = self.orientation_detector.detect(image)
        history.append(stage_result)
        return corrected_image

    def _run_lighting_normalization(self, image: Image.Image, history: List[StageResult]) -> Image.Image:
        if not self.config.lighting_normalization.enabled:
            history.append(StageResult(name="lighting_normalization", status="skipped", details={}))
            return image
        normalized_image, stage_result = self.lighting_normalizer.normalize(image)
        history.append(stage_result)
        return normalized_image

    def _run_optional_stage(
        self,
        image: Image.Image,
        config: StageConfig,
        stage_callable,
        history: List[StageResult],
        stage_name: str,
    ) -> Image.Image:
        if not config.enabled:
            history.append(StageResult(name=stage_name, status="skipped", details={}))
            return image
        output_image, stage_result = stage_callable(image)
        history.append(stage_result)
        return output_image

    def _run_additional_stages(self, image: Image.Image, history: List[StageResult]) -> Image.Image:
        for stage in self.additional_stages:
            context = StageContext(stage_name=stage.name, enabled=True, config={})
            output_image, stage_result = stage.execute(image, context)
            history.append(stage_result)
            image = output_image
        return image
