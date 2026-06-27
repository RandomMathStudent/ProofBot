"""Handwriting OCR package for ProofBot."""

from .interfaces import OCRModel
from .recognizers import SimpleOCRModel
from .models import ParagraphText

__all__ = ["OCRModel", "ParagraphText", "SimpleOCRModel"]
