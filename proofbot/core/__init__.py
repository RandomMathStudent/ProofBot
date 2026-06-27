"""ProofBot core infrastructure package.

Provides shared configuration loading, pipeline configuration, interface definitions,
logging helpers, and shared utilities.
"""

from .config import ConfigLoader, ProofBotConfig
from .exceptions import ProofBotError
from .interfaces import BackendFactory, StageFactory
from .pipeline import ProofBotPipeline
from .registry import Registry
from .utils import load_yaml_config

__all__ = [
    "ConfigLoader",
    "ProofBotConfig",
    "ProofBotError",
    "BackendFactory",
    "StageFactory",
    "ProofBotPipeline",
    "Registry",
    "load_yaml_config",
]
