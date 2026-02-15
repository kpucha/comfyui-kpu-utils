"""KPU example node for comfyui-kpu-utils.

This file defines a minimal, functional ComfyUI-style node class
that converts images to grayscale. Handles PyTorch tensors, numpy arrays,
and PIL Images.
"""
from typing import Any, Dict
from PIL import Image
import numpy as np

try:
    import torch
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False


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
        """Convert `image` to grayscale (replicated to 3 channels for compatibility).

        Handles:
        - PyTorch tensors (batch, height, width, 3) -> (batch, height, width, 3) with R=G=B
        - numpy arrays (height, width, 3) -> (height, width, 3) with R=G=B
        - PIL Image
        """
        try:
            # PyTorch tensor (most common in ComfyUI)
            if HAS_TORCH and isinstance(image, torch.Tensor):
                # Assume shape (batch, height, width, channels) with float [0, 1]
                print(f"[KPUExampleNode] Input tensor shape: {image.shape}, dtype: {image.dtype}")
                
                # Convert RGB to grayscale using standard formula
                # gray = 0.299*R + 0.587*G + 0.114*B
                if image.shape[-1] >= 3:  # RGB or RGBA
                    gray = (0.299 * image[..., 0] + 
                            0.587 * image[..., 1] + 
                            0.114 * image[..., 2])
                else:
                    gray = image[..., 0]  # Already single channel
                
                # Replicate gray to 3 channels (R=G=B) for compatibility
                # Stack along last dimension: (batch, height, width) -> (batch, height, width, 3)
                gray_3ch = torch.stack([gray, gray, gray], dim=-1)
                print(f"[KPUExampleNode] Output tensor shape: {gray_3ch.shape}")
                return (gray_3ch,)
            
            # PIL Image -> return PIL grayscale
            if isinstance(image, Image.Image):
                gray_pil = image.convert("L")
                # Convert back to RGB to keep 3 channels
                rgb_pil = Image.new("RGB", gray_pil.size)
                rgb_pil.paste(gray_pil)
                return (rgb_pil,)

            # numpy array
            if isinstance(image, np.ndarray):
                print(f"[KPUExampleNode] Input numpy array shape: {image.shape}, dtype: {image.dtype}")
                orig_dtype = image.dtype
                
                # Handle different shapes: (H,W,C) or (H,W)
                if len(image.shape) == 3 and image.shape[-1] >= 3:
                    # RGB/RGBA to grayscale
                    if np.issubdtype(orig_dtype, np.floating):
                        # Assume normalized [0, 1]
                        gray = (0.299 * image[..., 0] + 
                                0.587 * image[..., 1] + 
                                0.114 * image[..., 2])
                    else:
                        # uint8 [0, 255]
                        gray = (0.299 * image[..., 0] + 
                                0.587 * image[..., 1] + 
                                0.114 * image[..., 2]).astype(orig_dtype)
                    
                    # Replicate to 3 channels
                    gray_3ch = np.stack([gray, gray, gray], axis=-1)
                else:
                    # Already single channel, replicate to 3
                    if len(image.shape) == 2:
                        gray_3ch = np.stack([image, image, image], axis=-1)
                    else:
                        gray_3ch = image
                
                print(f"[KPUExampleNode] Output numpy array shape: {gray_3ch.shape}")
                return (gray_3ch,)

            # Fallback: try to coerce to tensor or numpy
            if HAS_TORCH:
                try:
                    tensor = torch.from_numpy(np.array(image))
                    return self.process(tensor)
                except Exception:
                    pass
            
            return (image,)
        except Exception as e:
            print(f"[KPUExampleNode] Error in process: {e}")
            import traceback
            traceback.print_exc()
            return (image,)
