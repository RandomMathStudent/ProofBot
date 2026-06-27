from __future__ import annotations

from PIL import Image

from .models import Denoiser, StageResult


class BasicDenoiser(Denoiser):
    @property
    def name(self) -> str:
        return "basic_denoiser"

    def denoise(self, image: Image.Image) -> tuple[Image.Image, StageResult]:
        result = StageResult(name=self.name, status="completed", details={"method": "pass_through"})
        return image, result
