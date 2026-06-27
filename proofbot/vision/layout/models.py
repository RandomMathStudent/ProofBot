from __future__ import annotations

from dataclasses import dataclass
from typing import List

from proofbot.models import BoundingBox, DocumentLayout, LayoutRegion, RegionType


@dataclass(frozen=True)
class LayoutModels:
    layout: DocumentLayout
    regions: List[LayoutRegion]
