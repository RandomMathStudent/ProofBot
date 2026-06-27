from __future__ import annotations

from proofbot.models import DocumentLayout, LayoutRegion, RegionType, BoundingBox, NormalizedImage
from .interfaces import LayoutDetector
from .models import LayoutModels


class SimpleLayoutDetector(LayoutDetector):
    @property
    def name(self) -> str:
        return "simple_layout_detector"

    def detect(self, image: NormalizedImage) -> DocumentLayout:
        region = LayoutRegion(
            region_id="page-0-paragraph-0",
            region_type=RegionType.PARAGRAPH,
            bbox=BoundingBox(x=0.0, y=0.0, width=1.0, height=1.0),
            confidence=0.5,
        )
        return DocumentLayout(image_id=image.metadata.source, regions=[region])
