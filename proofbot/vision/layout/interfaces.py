from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import DocumentLayout, NormalizedImage


class LayoutDetector(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def detect(self, image: NormalizedImage) -> DocumentLayout:
        raise NotImplementedError
