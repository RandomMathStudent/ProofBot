from __future__ import annotations

from PIL import Image

from .models import StageResult, SuperResolver


class BasicSuperResolver(SuperResolver):
    @property
    def name(self) -> str:
        return "basic_super_resolver"

    def upscale(self, image: Image.Image) -> tuple[Image.Image, StageResult]:
        result = StageResult(name=self.name, status="completed", details={"method": "pass_through"})
        return image, result
