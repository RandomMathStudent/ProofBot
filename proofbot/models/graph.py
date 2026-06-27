from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List

from .ast import ProofNode


@dataclass(frozen=True)
class ProofGraphEdge:
    source_id: str
    target_id: str
    relation: str
    confidence: float
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ProofGraph:
    nodes: List[ProofNode] = field(default_factory=list)
    edges: List[ProofGraphEdge] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
