from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import DocumentLayout, ProofAST, VerificationReport
from proofbot.models import BoundingBox


class ErrorLocalizer(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def localize(
        self,
        report: VerificationReport,
        proof_ast: ProofAST,
        layout: DocumentLayout,
    ) -> list[BoundingBox]:
        raise NotImplementedError
