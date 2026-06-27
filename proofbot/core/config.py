from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ProofBotConfig:
    vision: dict[str, Any]
    layout: dict[str, Any]
    ocr: dict[str, Any]
    formula: dict[str, Any]
    ast: dict[str, Any]
    graph: dict[str, Any]
    autoformalization: dict[str, Any]
    lean: dict[str, Any]
    error_localization: dict[str, Any]


class ConfigLoader:
    @staticmethod
    def load(path: Path) -> ProofBotConfig:
        with path.open("r", encoding="utf-8") as stream:
            raw = yaml.safe_load(stream)
        return ProofBotConfig(
            vision=raw.get("vision", {}),
            layout=raw.get("layout", {}),
            ocr=raw.get("ocr", {}),
            formula=raw.get("formula", {}),
            ast=raw.get("ast", {}),
            graph=raw.get("graph", {}),
            autoformalization=raw.get("autoformalization", {}),
            lean=raw.get("lean", {}),
            error_localization=raw.get("error_localization", {}),
        )
