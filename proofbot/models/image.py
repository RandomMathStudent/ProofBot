from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image


@dataclass(frozen=True)
class ImageMetadata:
    source: str
    original_size: Tuple[int, int]
    mode: str
    dpi: Optional[Tuple[int, int]] = None
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class QualityReport:
    resolution_dpi: Optional[float]
    blur_score: Optional[float]
    brightness: Optional[float]
    contrast: Optional[float]
    glare_score: Optional[float]
    noise_level: Optional[float]
    recommendations: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class StageResult:
    name: str
    status: str
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class NormalizedImage:
    image: Image.Image
    metadata: ImageMetadata
    quality_report: QualityReport
    page_polygons: List[Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float], Tuple[float, float]]]
    preprocessing_history: List[StageResult] = field(default_factory=list)
