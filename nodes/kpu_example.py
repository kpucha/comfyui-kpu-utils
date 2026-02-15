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
        - If `image` is a `numpy.ndarray`, handles both normalized floats [0,1]
          and uint8 [0,255]. Returns HWC format with single channel.
        - On any error, returns the original `image`.
        """
        try:
            # PIL Image -> return PIL grayscale
            if isinstance(image, Image.Image):
                return (image.convert("L"),)

            # numpy array -> handle ComfyUI format (HWC float or uint8)
            if isinstance(image, np.ndarray):
                orig_dtype = image.dtype
                
                # Normalize to uint8 [0, 255] for PIL conversion
                if np.issubdtype(orig_dtype, np.floating):
                    # Assume normalized [0, 1]
                    img_uint8 = (np.clip(image, 0, 1) * 255).astype(np.uint8)
                else:
                    img_uint8 = image.astype(np.uint8)
                
                # Convert to PIL, apply grayscale
                pil = Image.fromarray(img_uint8)
                gray_pil = pil.convert("L")
                gray_arr = np.array(gray_pil)  # HW format (2D)
                
                # Convert back to original dtype and restore HWC format
                if np.issubdtype(orig_dtype, np.floating):
                    # Return float [0, 1], expand to HWC
                    gray_float = (gray_arr.astype(np.float32) / 255.0)
                    out = np.expand_dims(gray_float, axis=2)
                else:
                    # Return uint8, expand to HWC
                    out = np.expand_dims(gray_arr.astype(orig_dtype), axis=2)
                
                return (out,)

            # Fallback: try to coerce to numpy and behave like above
            arr = np.array(image)
            orig_dtype = arr.dtype
            
            if np.issubdtype(orig_dtype, np.floating):
                img_uint8 = (np.clip(arr, 0, 1) * 255).astype(np.uint8)
            else:
                img_uint8 = arr.astype(np.uint8)
            
            pil = Image.fromarray(img_uint8)
            gray_pil = pil.convert("L")
            gray_arr = np.array(gray_pil)
            
            if np.issubdtype(orig_dtype, np.floating):
                gray_float = (gray_arr.astype(np.float32) / 255.0)
                out = np.expand_dims(gray_float, axis=2)
            else:
                out = np.expand_dims(gray_arr.astype(orig_dtype), axis=2)

            return (out,)
        except Exception as e:
            print(f"Error in KPUExampleNode.process: {e}")
            return (image,)
