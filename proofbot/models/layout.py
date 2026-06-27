from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List, Tuple


class RegionType(str, Enum):
    PARAGRAPH = "paragraph"
    THEOREM = "theorem"
    PROOF = "proof"
    EQUATION = "equation"
    DIAGRAM = "diagram"
    TITLE = "title"
    SECTION = "section"
    MARGIN_NOTE = "margin_note"


@dataclass(frozen=True)
class BoundingBox:
    x: float
    y: float
    width: float
    height: float


@dataclass(frozen=True)
class LayoutRegion:
    region_id: str
    region_type: RegionType
    bbox: BoundingBox
    confidence: float
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DocumentLayout:
    image_id: str
    regions: List[LayoutRegion] = field(default_factory=list)


PagePolygon = Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float], Tuple[float, float]]
