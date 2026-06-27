from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(frozen=True)
class ParagraphText:
    region_id: str
    text: str
    confidence: float
    metadata: Dict[str, Any] = field(default_factory=dict)
