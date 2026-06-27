from __future__ import annotations

from typing import List, Tuple

from PIL import Image

from .models import DocumentDetector, PageDetection, StageResult


class BasicDocumentDetector(DocumentDetector):
    @property
    def name(self) -> str:
        return "basic_document_detector"

    def detect(self, image: Image.Image) -> Tuple[List[PageDetection], StageResult]:
        width, height = image.size
        page = PageDetection(
            polygon=((0.0, 0.0), (width, 0.0), (width, height), (0.0, height)),
            confidence=0.9,
            page_id=0,
            metadata={"detected_as_full_frame": True},
        )
        result = StageResult(
            name=self.name,
            status="completed",
            details={"page_count": 1, "best_confidence": page.confidence},
        )
        return [page], result
