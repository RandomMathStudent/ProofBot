from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class Formula:
    region_id: str
    latex: str
    mathml: Optional[str]
    confidence: float
    metadata: Dict[str, Any] = field(default_factory=dict)
