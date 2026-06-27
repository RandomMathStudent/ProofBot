from __future__ import annotations

from proofbot.models import ParagraphText, NormalizedImage
from .interfaces import OCRModel


class SimpleOCRModel(OCRModel):
    @property
    def name(self) -> str:
        return "simple_ocr_model"

    def transcribe(self, image: NormalizedImage, region: str) -> ParagraphText:
        return ParagraphText(region_id=region, text="", confidence=0.0)
