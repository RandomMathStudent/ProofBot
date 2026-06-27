from __future__ import annotations

from typing import Any, Callable


class Registry:
    def __init__(self) -> None:
        self._registry: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, factory: Callable[..., Any]) -> None:
        self._registry[name] = factory

    def create(self, name: str, *args: object, **kwargs: object) -> Any:
        if name not in self._registry:
            raise KeyError(f"No registered implementation for: {name}")
        return self._registry[name](*args, **kwargs)

    def available(self) -> list[str]:
        return sorted(self._registry.keys())
