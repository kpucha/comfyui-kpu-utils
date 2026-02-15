"""comfyui-kpu-utils package.

A collection of custom nodes for ComfyUI focused on KPU utilities.
"""

from .nodes import KPUExampleNode

# Required by ComfyUI to recognize custom nodes
NODE_CLASS_MAPPINGS = {
    "KPUExampleNode": KPUExampleNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KPUExampleNode": "KPU Example (Grayscale)",
}

__all__ = ["KPUExampleNode", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
