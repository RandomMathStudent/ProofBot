from __future__ import annotations

from proofbot.models import Formula, NormalizedImage
from .interfaces import FormulaRecognizer


class SimpleFormulaRecognizer(FormulaRecognizer):
    @property
    def name(self) -> str:
        return "simple_formula_recognizer"

    def recognize(self, image: NormalizedImage, region: str) -> Formula:
        return Formula(region_id=region, latex="", mathml=None, confidence=0.0)
