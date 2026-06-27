from __future__ import annotations

from typing import Any, Dict, Tuple, Union

import numpy as np
from PIL import Image, ImageOps


ImageInput = Union[str, Image.Image, np.ndarray]


def is_numpy_image(value: Any) -> bool:
    return isinstance(value, np.ndarray)


def is_pil_image(value: Any) -> bool:
    return isinstance(value, Image.Image)


def normalize_image_input(image_input: ImageInput) -> Image.Image:
    if isinstance(image_input, Image.Image):
        return image_input.convert("RGB")
    if isinstance(image_input, np.ndarray):
        array = image_input
        if array.ndim == 2:
            return Image.fromarray(array).convert("RGB")
        if array.ndim == 3 and array.shape[2] in {1, 3, 4}:
            return Image.fromarray(array.astype("uint8"))
        raise ValueError("Unsupported NumPy image shape: %s" % (array.shape,))
    if isinstance(image_input, str):
        return Image.open(image_input).convert("RGB")
    raise TypeError("Unsupported image input type: %r" % (type(image_input),))


def extract_metadata(image: Image.Image, source: str = "unknown") -> Dict[str, Any]:
    metadata: Dict[str, Any] = {"source": source, "mode": image.mode, "size": image.size}
    if hasattr(image, "info"):
        metadata.update({k: v for k, v in image.info.items() if k not in metadata})
    return metadata


def ensure_rgb(image: Image.Image) -> Image.Image:
    if image.mode != "RGB":
        return image.convert("RGB")
    return image


def clamp_value(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    return max(min(value, maximum), minimum)
