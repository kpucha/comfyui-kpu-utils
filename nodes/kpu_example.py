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
        """Convert `image` to grayscale.

        Handles:
        - PyTorch tensors (batch, height, width, 3) -> (batch, height, width, 1)
        - numpy arrays (height, width, 3) -> (height, width, 1)
        - PIL Image
        """
        try:
            # PyTorch tensor (most common in ComfyUI)
            if HAS_TORCH and isinstance(image, torch.Tensor):
                # Assume shape (batch, height, width, channels) with float [0, 1]
                print(f"[KPUExampleNode] Input tensor shape: {image.shape}, dtype: {image.dtype}")
                
                # Convert RGB to grayscale using standard formula
                # gray = 0.299*R + 0.587*G + 0.114*B
                if image.shape[-1] == 3:  # RGB
                    gray = (0.299 * image[..., 0] + 
                            0.587 * image[..., 1] + 
                            0.114 * image[..., 2])
                elif image.shape[-1] == 4:  # RGBA
                    gray = (0.299 * image[..., 0] + 
                            0.587 * image[..., 1] + 
                            0.114 * image[..., 2])
                else:
                    gray = image[..., 0]  # Already single channel
                
                # Expand dims to maintain (batch, height, width, 1)
                gray = gray.unsqueeze(-1)
                print(f"[KPUExampleNode] Output tensor shape: {gray.shape}")
                return (gray,)
            
            # PIL Image -> return PIL grayscale
            if isinstance(image, Image.Image):
                return (image.convert("L"),)

            # numpy array
            if isinstance(image, np.ndarray):
                print(f"[KPUExampleNode] Input numpy array shape: {image.shape}, dtype: {image.dtype}")
                orig_dtype = image.dtype
                
                # Handle different shapes: (H,W,C) or (H,W)
                if len(image.shape) == 3 and image.shape[-1] in (3, 4):
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
                    
                    # Expand dims to HWC
                    gray = np.expand_dims(gray, axis=2)
                else:
                    # Already grayscale or single channel
                    gray = image
                
                print(f"[KPUExampleNode] Output numpy array shape: {gray.shape}")
                return (gray,)

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
