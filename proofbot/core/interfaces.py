from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from proofbot.models import NormalizedImage


class BackendFactory(ABC):
    @abstractmethod
    def create(self, backend_name: str, config: dict[str, Any]) -> Any:
        raise NotImplementedError


class StageFactory(ABC):
    @abstractmethod
    def create(self, stage_name: str, backend_name: str, config: dict[str, Any]) -> Any:
        raise NotImplementedError
