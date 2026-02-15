"""comfyui-kpu-utils package.

A collection of custom nodes for ComfyUI focused on KPU utilities.
"""

from .nodes import KPUExampleNode, WailustriousPromptGenerator, WailustriousPromptBuilder, WailustriousMultiCharacterGenerator

# Required by ComfyUI to recognize custom nodes
NODE_CLASS_MAPPINGS = {
    "KPUExampleNode": KPUExampleNode,
    "WailustriousPromptGenerator": WailustriousPromptGenerator,
    "WailustriousPromptBuilder": WailustriousPromptBuilder,
    "WailustriousMultiCharacterGenerator": WailustriousMultiCharacterGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KPUExampleNode": "KPU Example (Grayscale)",
    "WailustriousPromptGenerator": "KPU Wailustrious Prompt Generator",
    "WailustriousPromptBuilder": "KPU Wailustrious Prompt Builder (Presets)",
    "WailustriousMultiCharacterGenerator": "KPU Wailustrious Multi-Character Generator",
}

__all__ = ["KPUExampleNode", "WailustriousPromptGenerator", "WailustriousPromptBuilder", "WailustriousMultiCharacterGenerator", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
