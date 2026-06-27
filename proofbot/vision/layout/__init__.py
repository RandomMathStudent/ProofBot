"""Layout detection package for ProofBot."""

from .detectors import SimpleLayoutDetector
from .interfaces import LayoutDetector
from .models import DocumentLayout, LayoutRegion, RegionType

__all__ = ["LayoutDetector", "DocumentLayout", "LayoutRegion", "RegionType", "SimpleLayoutDetector"]
