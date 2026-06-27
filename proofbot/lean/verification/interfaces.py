from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import LeanProgram, VerificationReport


class LeanVerifier(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def verify(self, program: LeanProgram) -> VerificationReport:
        raise NotImplementedError
