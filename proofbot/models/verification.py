from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class VerificationDiagnostic:
    line: int
    column: int
    severity: str
    message: str
    code: Optional[str] = None
    ast_node_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class VerificationReport:
    success: bool
    diagnostics: List[VerificationDiagnostic] = field(default_factory=list)
    runtime_ms: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
