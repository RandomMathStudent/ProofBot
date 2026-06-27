from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import LeanIntermediateRepresentation, ProofAST, ProofGraph


class AutoformalizerBackend(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def formalize(
        self,
        proof_ast: ProofAST,
        proof_graph: ProofGraph,
    ) -> LeanIntermediateRepresentation:
        raise NotImplementedError
