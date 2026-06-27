from __future__ import annotations

from PIL import Image

from .models import PageDetection, PerspectiveCorrector, StageResult


class BasicPerspectiveCorrector(PerspectiveCorrector):
    @property
    def name(self) -> str:
        return "basic_perspective_corrector"

    def correct(self, image: Image.Image, page: PageDetection) -> tuple[Image.Image, StageResult]:
        result = StageResult(
            name=self.name,
            status="completed",
            details={"page_id": page.page_id, "polygon": page.polygon},
        )
        return image, result
