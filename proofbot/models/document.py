from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Tuple

from .layout import LayoutRegion


@dataclass(frozen=True)
class PagePolygon:
    points: Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float], Tuple[float, float]]
    confidence: float
    page_id: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DocumentMetadata:
    image_id: str
    page_count: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DocumentLayout:
    image_id: str
    regions: List[LayoutRegion] = field(default_factory=list)
    page_polygons: List[PagePolygon] = field(default_factory=list)
