from __future__ import annotations

from proofbot.models import DocumentLayout, Formula, ParagraphText, ProofAST, ProofNode, ProofNodeType
from .interfaces import ProofASTBuilder


class SimpleProofASTBuilder(ProofASTBuilder):
    @property
    def name(self) -> str:
        return "simple_proof_ast_builder"

    def build(
        self,
        layout: DocumentLayout,
        paragraphs: list[ParagraphText],
        formulas: list[Formula],
    ) -> ProofAST:
        nodes = []
        for paragraph in paragraphs:
            nodes.append(
                ProofNode(
                    node_id=paragraph.region_id,
                    node_type=ProofNodeType.PARAGRAPH,
                    source_region_id=paragraph.region_id,
                    text=paragraph.text,
                )
            )
        for formula in formulas:
            nodes.append(
                ProofNode(
                    node_id=formula.region_id,
                    node_type=ProofNodeType.EQUATION,
                    source_region_id=formula.region_id,
                    formula=formula.latex,
                )
            )
        return ProofAST(nodes=nodes, root_id=nodes[0].node_id if nodes else None)
