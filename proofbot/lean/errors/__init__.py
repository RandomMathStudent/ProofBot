"""Lean error localization package."""

from .localization import ErrorLocalizer
from .interfaces import ErrorLocalizer as ErrorLocalizerInterface

__all__ = ["ErrorLocalizer", "ErrorLocalizerInterface"]
