from __future__ import annotations

import logging
from typing import Any


def configure_logger(name: str = "proofbot", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def stage_log_message(stage_name: str, message: str, **data: Any) -> str:
    details = " ".join(f"{key}={value}" for key, value in data.items())
    return f"[{stage_name}] {message} {details}".strip()
