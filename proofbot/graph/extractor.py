from __future__ import annotations

from proofbot.models import ProofAST, ProofGraph, ProofGraphEdge
from .interfaces import ProofGraphExtractor


class SimpleProofGraphExtractor(ProofGraphExtractor):
    @property
    def name(self) -> str:
        return "simple_proof_graph_extractor"

    def extract(self, proof_ast: ProofAST) -> ProofGraph:
        edges = []
        if len(proof_ast.nodes) >= 2:
            for first, second in zip(proof_ast.nodes, proof_ast.nodes[1:]):
                edges.append(
                    ProofGraphEdge(
                        source_id=first.node_id,
                        target_id=second.node_id,
                        relation="sequential",
                        confidence=0.5,
                    )
                )
        return ProofGraph(nodes=proof_ast.nodes, edges=edges)
