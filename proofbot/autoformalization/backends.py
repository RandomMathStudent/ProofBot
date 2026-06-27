from __future__ import annotations

from proofbot.models import LeanIntermediateRepresentation, ProofAST, ProofGraph
from .interfaces import AutoformalizerBackend


class LLMBackend(AutoformalizerBackend):
    @property
    def name(self) -> str:
        return "llm_backend"

    def formalize(
        self,
        proof_ast: ProofAST,
        proof_graph: ProofGraph,
    ) -> LeanIntermediateRepresentation:
        return LeanIntermediateRepresentation(statements="", metadata={})
