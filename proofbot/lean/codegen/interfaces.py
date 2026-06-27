from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import LeanIntermediateRepresentation, LeanProgram


class LeanCodeGenerator(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate(self, lean_ir: LeanIntermediateRepresentation) -> LeanProgram:
        raise NotImplementedError
