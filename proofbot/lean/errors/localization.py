from __future__ import annotations

from proofbot.models import BoundingBox, DocumentLayout, ProofAST, VerificationReport
from .interfaces import ErrorLocalizer


class SimpleErrorLocalizer(ErrorLocalizer):
    @property
    def name(self) -> str:
        return "simple_error_localizer"

    def localize(
        self,
        report: VerificationReport,
        proof_ast: ProofAST,
        layout: DocumentLayout,
    ) -> list[BoundingBox]:
        return []
