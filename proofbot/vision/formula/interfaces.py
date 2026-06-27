from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import Formula, NormalizedImage


class FormulaRecognizer(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def recognize(self, image: NormalizedImage, region: str) -> Formula:
        raise NotImplementedError
