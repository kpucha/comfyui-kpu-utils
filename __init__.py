"""comfyui-kpu-utils package.

A collection of custom nodes for ComfyUI focused on KPU utilities.
"""

from .nodes import (
    KPUExampleNode,
    WailustriousPromptGenerator,
    WailustriousPromptBuilder,
    WailustriousCharacterBuilder,
    WailustriousMultiCharacterGenerator,
    KPUSceneGenerator
)

# Required by ComfyUI to recognize custom nodes
NODE_CLASS_MAPPINGS = {
    "KPUExampleNode": KPUExampleNode,
    "WailustriousPromptGenerator": WailustriousPromptGenerator,
    "WailustriousPromptBuilder": WailustriousPromptBuilder,
    "WailustriousCharacterBuilder": WailustriousCharacterBuilder,
    "WailustriousMultiCharacterGenerator": WailustriousMultiCharacterGenerator,
    "KPUSceneGenerator": KPUSceneGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KPUExampleNode": "KPU Example (Grayscale)",
    "WailustriousPromptGenerator": "KPU Wailustrious Prompt Generator",
    "WailustriousPromptBuilder": "KPU Wailustrious Prompt Builder (Presets)",
    "WailustriousCharacterBuilder": "KPU Wailustrious Character Builder",
    "WailustriousMultiCharacterGenerator": "KPU Wailustrious Multi-Character Scene",
    "KPUSceneGenerator": "KPU Scene Generator",
}

__all__ = [
    "KPUExampleNode",
    "WailustriousPromptGenerator",
    "WailustriousPromptBuilder",
    "WailustriousCharacterBuilder",
    "WailustriousMultiCharacterGenerator",
    "KPUSceneGenerator",
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]
