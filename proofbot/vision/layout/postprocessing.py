from __future__ import annotations

from proofbot.models import DocumentLayout


def filter_regions_by_confidence(layout: DocumentLayout, threshold: float) -> DocumentLayout:
    filtered = [region for region in layout.regions if region.confidence >= threshold]
    return DocumentLayout(image_id=layout.image_id, regions=filtered)
