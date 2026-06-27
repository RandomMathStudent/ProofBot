from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

from PIL import Image
import numpy as np

ImageInput = Union[str, Image.Image, np.ndarray]


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
class PageDetection:
    polygon: Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float], Tuple[float, float]]
    confidence: float
    page_id: int
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class StageContext:
    stage_name: str
    enabled: bool
    config: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class StageResult:
    name: str
    status: str
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PreprocessingResult:
    image: Image.Image
    metadata: ImageMetadata
    quality: QualityReport
    pages: List[PageDetection]
    history: List[StageResult]
    config: Dict[str, Any] = field(default_factory=dict)


class BaseStage(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def execute(self, image: Image.Image, context: StageContext) -> Tuple[Image.Image, StageResult]:
        raise NotImplementedError


class ImageLoader(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def load(self, image_input: ImageInput) -> Tuple[Image.Image, ImageMetadata]:
        raise NotImplementedError


class QualityEstimator(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def estimate(self, image: Image.Image, metadata: ImageMetadata) -> QualityReport:
        raise NotImplementedError


class DocumentDetector(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def detect(self, image: Image.Image) -> Tuple[List[PageDetection], StageResult]:
        raise NotImplementedError


class PerspectiveCorrector(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def correct(self, image: Image.Image, page: PageDetection) -> Tuple[Image.Image, StageResult]:
        raise NotImplementedError


class OrientationDetector(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def detect(self, image: Image.Image) -> Tuple[Image.Image, StageResult]:
        raise NotImplementedError


class LightingNormalizer(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def normalize(self, image: Image.Image) -> Tuple[Image.Image, StageResult]:
        raise NotImplementedError


class Denoiser(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def denoise(self, image: Image.Image) -> Tuple[Image.Image, StageResult]:
        raise NotImplementedError


class SuperResolver(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def upscale(self, image: Image.Image) -> Tuple[Image.Image, StageResult]:
        raise NotImplementedError
