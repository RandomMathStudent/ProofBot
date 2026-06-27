from __future__ import annotations

from proofbot.models import LeanProgram, VerificationReport
from .interfaces import LeanVerifier


class SimpleLeanVerifier(LeanVerifier):
    @property
    def name(self) -> str:
        return "simple_lean_verifier"

    def verify(self, program: LeanProgram) -> VerificationReport:
        return VerificationReport(success=True, diagnostics=[], metadata={})
