from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class LeanIntermediateRepresentation:
    statements: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class LeanProgram:
    source: str
    module_name: str
    metadata: Dict[str, Any] = field(default_factory=dict)
