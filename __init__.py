"""comfyui-kpu-utils package.

A collection of custom nodes for ComfyUI focused on KPU utilities.
"""

from .nodes import KPUExampleNode, WailustriousPromptGenerator, WailustriousPromptBuilder

# Required by ComfyUI to recognize custom nodes
NODE_CLASS_MAPPINGS = {
    "KPUExampleNode": KPUExampleNode,
    "WailustriousPromptGenerator": WailustriousPromptGenerator,
    "WailustriousPromptBuilder": WailustriousPromptBuilder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KPUExampleNode": "KPU Example (Grayscale)",
    "WailustriousPromptGenerator": "KPU Wailustrious Prompt Generator",
    "WailustriousPromptBuilder": "KPU Wailustrious Prompt Builder (Presets)",
}

__all__ = ["KPUExampleNode", "WailustriousPromptGenerator", "WailustriousPromptBuilder", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
