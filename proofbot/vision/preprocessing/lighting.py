from __future__ import annotations

from PIL import Image, ImageEnhance

from .models import LightingNormalizer, StageResult


class BasicLightingNormalizer(LightingNormalizer):
    @property
    def name(self) -> str:
        return "basic_lighting_normalizer"

    def normalize(self, image: Image.Image) -> tuple[Image.Image, StageResult]:
        enhancer = ImageEnhance.Brightness(image)
        normalized = enhancer.enhance(1.0)
        result = StageResult(name=self.name, status="completed", details={"method": "pass_through"})
        return normalized, result
