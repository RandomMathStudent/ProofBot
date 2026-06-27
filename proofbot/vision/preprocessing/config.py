from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class StageConfig:
    enabled: bool = True
    params: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PreprocessingConfig:
    quality_assessment: StageConfig = StageConfig()
    document_detection: StageConfig = StageConfig()
    perspective_correction: StageConfig = StageConfig()
    orientation_detection: StageConfig = StageConfig()
    lighting_normalization: StageConfig = StageConfig()
    denoise: StageConfig = StageConfig(enabled=False)
    super_resolution: StageConfig = StageConfig(enabled=False)
    preserve_metadata: bool = True
    page_limit: Optional[int] = None
    use_default_stages: bool = True

    def with_overrides(self, **overrides: Any) -> "PreprocessingConfig":
        return PreprocessingConfig(**{**self.__dict__, **overrides})
