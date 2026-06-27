"""Lean code generation subpackage."""

from .generator import LeanCodeGenerator
from .interfaces import LeanCodeGenerator as LeanCodeGeneratorInterface

__all__ = ["LeanCodeGenerator", "LeanCodeGeneratorInterface"]
