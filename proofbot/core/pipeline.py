from __future__ import annotations

from typing import Any, Iterable

from .config import ProofBotConfig
from .exceptions import ProofBotError
from .interfaces import StageFactory
from .registry import Registry


class ProofBotPipeline:
    def __init__(
        self,
        config: ProofBotConfig,
        stage_factory: StageFactory,
        registry: Registry,
    ) -> None:
        self.config = config
        self.stage_factory = stage_factory
        self.registry = registry

    def build(self) -> list[Any]:
        stages: list[Any] = []
        stage_order = [
            "vision.preprocessing",
            "vision.layout",
            "vision.ocr",
            "vision.formula",
            "ast",
            "graph",
            "autoformalization",
            "lean.codegen",
            "lean.verification",
            "error_localization",
        ]
        for stage_name in stage_order:
            stage_config = self._fetch_stage_config(stage_name)
            implementation = self.stage_factory.create(stage_name, stage_config.get("backend", "default"), stage_config)
            stages.append(implementation)
        return stages

    def _fetch_stage_config(self, stage_name: str) -> dict[str, Any]:
        mapping = {
            "vision.preprocessing": self.config.vision.get("preprocessing", {}),
            "vision.layout": self.config.layout,
            "vision.ocr": self.config.ocr,
            "vision.formula": self.config.formula,
            "ast": self.config.ast,
            "graph": self.config.graph,
            "autoformalization": self.config.autoformalization,
            "lean.codegen": self.config.lean.get("codegen", {}),
            "lean.verification": self.config.lean.get("verification", {}),
            "error_localization": self.config.error_localization,
        }
        if stage_name not in mapping:
            raise ProofBotError(f"Unknown pipeline stage: {stage_name}")
        return mapping[stage_name]
