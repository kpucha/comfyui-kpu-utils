"""KPU example node for comfyui-kpu-utils.

This file defines a minimal, functional ComfyUI-style node class
that acts as a pass-through for an image input. It's intended as a
template for building more advanced KPU-related nodes.
"""
from typing import Any, Dict
from PIL import Image
import numpy as np


class KPUExampleNode:
    """A minimal example ComfyUI node that converts images to grayscale.

    - Accepts one `IMAGE` input (PIL.Image or numpy array).
    - Returns a grayscale image of the same type as the input.
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        return {"required": {"image": ("IMAGE",)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "process"
    CATEGORY = "KPU Utils"

    def process(self, image: Any):
        """Convert `image` to grayscale and return it with the same type.

        - If `image` is a `PIL.Image`, returns a `PIL.Image` in mode "L".
        - If `image` is a `numpy.ndarray`, returns a 2D numpy array
          (grayscale). If the original array was floating, the result is
          returned as floats in [0, 1]; integer arrays are returned in
          the original integer dtype (0-255).
        - On any error, returns the original `image`.
        """
        try:
            # PIL Image -> return PIL grayscale
            if isinstance(image, Image.Image):
                return (image.convert("L"),)

            # numpy array -> convert to PIL, convert, then map back dtype
            if isinstance(image, np.ndarray):
                orig_dtype = image.dtype
                pil = Image.fromarray(image)
                gray_pil = pil.convert("L")
                gray_arr = np.array(gray_pil)

                if np.issubdtype(orig_dtype, np.floating):
                    out = (gray_arr.astype(np.float32) / 255.0)
                else:
                    out = gray_arr.astype(orig_dtype)

                return (out,)

            # Fallback: try to coerce to numpy and behave like above
            arr = np.array(image)
            orig_dtype = arr.dtype
            pil = Image.fromarray(arr)
            gray_pil = pil.convert("L")
            gray_arr = np.array(gray_pil)

            if np.issubdtype(orig_dtype, np.floating):
                out = (gray_arr.astype(np.float32) / 255.0)
            else:
                out = gray_arr.astype(orig_dtype)

            return (out,)
        except Exception:
            return (image,)
