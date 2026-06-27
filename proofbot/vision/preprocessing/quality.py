from __future__ import annotations

from PIL import Image

from .models import ImageMetadata, QualityReport, QualityEstimator, StageResult


class BasicQualityEstimator(QualityEstimator):
    @property
    def name(self) -> str:
        return "basic_quality_estimator"

    def estimate(self, image: Image.Image, metadata: ImageMetadata) -> QualityReport:
        width, height = image.size
        resolution_dpi = metadata.dpi[0] if metadata.dpi else None
        blur_score = 0.5
        brightness = 0.5
        contrast = 0.5
        glare_score = 0.0
        noise_level = 0.0
        return QualityReport(
            resolution_dpi=resolution_dpi,
            blur_score=blur_score,
            brightness=brightness,
            contrast=contrast,
            glare_score=glare_score,
            noise_level=noise_level,
            recommendations=[
                "Enable higher-resolution acquisition if resolution_dpi is low.",
                "Avoid direct glare from lighting fixtures.",
            ],
        )

    def report_stage(self) -> StageResult:
        return StageResult(name=self.name, status="completed", details={})
