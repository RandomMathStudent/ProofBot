from __future__ import annotations

from PIL import Image

from .models import OrientationDetector, StageResult


class BasicOrientationDetector(OrientationDetector):
    @property
    def name(self) -> str:
        return "basic_orientation_detector"

    def detect(self, image: Image.Image) -> tuple[Image.Image, StageResult]:
        result = StageResult(name=self.name, status="completed", details={"rotation": 0})
        return image, result
