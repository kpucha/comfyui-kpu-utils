"""KPU Wailustrious Multi-Character Prompt Generator.

Combines pre-built character descriptions into a full scene prompt.
Works with the Character Builder node for modularity.
"""
from typing import Any, Dict, Tuple


class WailustriousMultiCharacterGenerator:
    """Combine multiple character descriptions into a complete scene prompt.
    
    Use the Character Builder node to create individual character descriptions,
    then feed them here along with scene settings.
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        return {
            "required": {
                # Character descriptions (from Character Builder)
                "character_1": ("STRING", {"default": "1girl, long black hair, blue eyes, school uniform, standing, smiling"}),
                
                # Scene Settings
                "location": ("STRING", {"default": "bedroom"}),
                "lighting": ("STRING", {"default": "soft lighting"}),
                "time_of_day": ("STRING", {"default": "daytime"}),
                
                "camera_angle": (
                    [
                        "eye level",
                        "dutch angle",
                        "low angle",
                        "high angle",
                        "overhead",
                        "POV",
                        "isometric",
                        "profile",
                        "3/4 view",
                    ],
                    {"default": "eye level"},
                ),
                
                # Art Quality
                "art_style": (["anime", "manga", "illustration", "pixelart"], {"default": "anime"}),
                "quality_tags": ("STRING", {"default": "high quality, masterpiece, detailed"}),
            },
            "optional": {
                "character_2": ("STRING", {"default": ""}),
                "character_3": ("STRING", {"default": ""}),
                "character_4": ("STRING", {"default": ""}),
                "character_5": ("STRING", {"default": ""}),
                "composition": ("STRING", {"default": ""}),  # e.g., "centered", "side by side"
                "scene_description": ("STRING", {"default": ""}),
                "negative_prompt": ("STRING", {"default": "ugly, deformed, blurry, lowres, watermark, text, extra fingers"}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "generate"
    CATEGORY = "KPU Utils"

    def generate(
        self,
        character_1: str,
        location: str,
        lighting: str,
        time_of_day: str,
        camera_angle: str,
        art_style: str,
        quality_tags: str,
        character_2: str = "",
        character_3: str = "",
        character_4: str = "",
        character_5: str = "",
        composition: str = "",
        scene_description: str = "",
        negative_prompt: str = "",
    ) -> Tuple[str, str]:
        """Generate multi-character scene prompt.
        
        Combines character descriptions with scene settings into a cohesive prompt.
        
        Returns:
            Tuple of (positive_prompt, negative_prompt) as strings.
        """
        
        prompt_parts = []
        
        # Add all non-empty character descriptions
        characters = [character_1, character_2, character_3, character_4, character_5]
        for char in characters:
            if char.strip():
                prompt_parts.append(char)
        
        # Camera angle
        if camera_angle.strip() and camera_angle != "eye level":
            prompt_parts.append(f"{camera_angle} view")
        
        # Composition
        if composition.strip():
            prompt_parts.append(composition)
        
        # Scene setting
        if location.strip():
            prompt_parts.append(location)
        if lighting.strip():
            prompt_parts.append(lighting)
        if time_of_day.strip():
            prompt_parts.append(time_of_day)
        
        # Scene description
        if scene_description.strip():
            prompt_parts.append(scene_description)
        
        # Art style and quality
        prompt_parts.append(art_style)
        if quality_tags.strip():
            prompt_parts.append(quality_tags)
        
        positive_prompt = ", ".join(part.strip() for part in prompt_parts if part.strip())
        
        # Ensure negative prompt is not empty
        if not negative_prompt.strip():
            negative_prompt = "ugly, deformed, blurry, lowres, watermark, text, extra fingers"
        
        return (positive_prompt, negative_prompt)

