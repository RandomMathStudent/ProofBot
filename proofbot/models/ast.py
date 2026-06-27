from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class ProofNodeType(str, Enum):
    PARAGRAPH = "paragraph"
    EQUATION = "equation"
    ASSUMPTION = "assumption"
    DEDUCTION = "deduction"
    CONCLUSION = "conclusion"
    THEOREM = "theorem"
    DEFINITION = "definition"


@dataclass(frozen=True)
class ProofNode:
    node_id: str
    node_type: ProofNodeType
    source_region_id: Optional[str]
    text: Optional[str] = None
    formula: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ProofAST:
    nodes: List[ProofNode] = field(default_factory=list)
    root_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
