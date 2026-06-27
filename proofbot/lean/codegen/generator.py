from __future__ import annotations

from proofbot.models import LeanIntermediateRepresentation, LeanProgram
from .interfaces import LeanCodeGenerator


class SimpleLeanCodeGenerator(LeanCodeGenerator):
    @property
    def name(self) -> str:
        return "simple_lean_code_generator"

    def generate(self, lean_ir: LeanIntermediateRepresentation) -> LeanProgram:
        return LeanProgram(source="", module_name="ProofBot", metadata=lean_ir.metadata)
