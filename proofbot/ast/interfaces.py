from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import DocumentLayout, Formula, ParagraphText, ProofAST


class ProofASTBuilder(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def build(
        self,
        layout: DocumentLayout,
        paragraphs: list[ParagraphText],
        formulas: list[Formula],
    ) -> ProofAST:
        raise NotImplementedError
