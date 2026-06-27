"""ProofBot vision preprocessing package.

This package defines a modular document image preprocessing pipeline for handwritten
mathematical proofs. It is intentionally designed around abstract stage interfaces
and configurable pipeline composition.
"""

from .pipeline import PreprocessingPipeline, PreprocessingResult
from .config import PreprocessingConfig, StageConfig
from .models import (
    ImageMetadata,
    QualityReport,
    PageDetection,
    StageContext,
    StageResult,
    BaseStage,
    ImageLoader,
    QualityEstimator,
    DocumentDetector,
    PerspectiveCorrector,
    OrientationDetector,
    LightingNormalizer,
    Denoiser,
    SuperResolver,
)

__all__ = [
    "PreprocessingPipeline",
    "PreprocessingResult",
    "PreprocessingConfig",
    "StageConfig",
    "ImageMetadata",
    "QualityReport",
    "PageDetection",
    "StageContext",
    "StageResult",
    "BaseStage",
    "ImageLoader",
    "QualityEstimator",
    "DocumentDetector",
    "PerspectiveCorrector",
    "OrientationDetector",
    "LightingNormalizer",
    "Denoiser",
    "SuperResolver",
]
