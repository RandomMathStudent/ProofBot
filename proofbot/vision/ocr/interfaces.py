from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import ParagraphText, DocumentLayout, NormalizedImage


class OCRModel(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def transcribe(self, image: NormalizedImage, region: str) -> ParagraphText:
        raise NotImplementedError
