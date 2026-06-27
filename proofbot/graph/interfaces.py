from __future__ import annotations

from abc import ABC, abstractmethod

from proofbot.models import ProofAST, ProofGraph


class ProofGraphExtractor(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def extract(self, proof_ast: ProofAST) -> ProofGraph:
        raise NotImplementedError
