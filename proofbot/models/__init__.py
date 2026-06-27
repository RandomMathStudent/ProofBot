"""Core data models for ProofBot.

This package exposes shared typed models used by all pipeline stages.
"""

from .ast import ProofAST
from .document import BoundingBox, DocumentLayout, PagePolygon
from .formula import Formula
from .graph import ProofGraph, ProofGraphEdge
from .image import ImageMetadata, NormalizedImage, QualityReport, StageResult
from .layout import LayoutRegion, RegionType
from .lean import LeanProgram, LeanIntermediateRepresentation
from .ocr import ParagraphText
from .verification import VerificationDiagnostic, VerificationReport

__all__ = [
    "BoundingBox",
    "DocumentLayout",
    "LayoutRegion",
    "PagePolygon",
    "Formula",
    "ProofAST",
    "ProofGraph",
    "ProofGraphEdge",
    "LeanProgram",
    "LeanIntermediateRepresentation",
    "ParagraphText",
    "ImageMetadata",
    "NormalizedImage",
    "QualityReport",
    "StageResult",
    "VerificationDiagnostic",
    "VerificationReport",
]
