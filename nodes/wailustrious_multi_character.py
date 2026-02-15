"""KPU Wailustrious Multi-Character Prompt Generator.

Combines pre-built character descriptions into a full scene prompt.
Automatically counts 1girl, 2girls, 1boy, etc. at the beginning.
"""
from typing import Any, Dict, Tuple


class WailustriousMultiCharacterGenerator:
    """Combine multiple character descriptions into a complete scene prompt.
    
    Use the Character Builder node to create individual character descriptions,
    then feed them here along with scene settings.
    Automatically handles character counting (1girl, 2girls, 1boy, etc).
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        return {
            "required": {
                # Character 1
                "character_1_desc": ("STRING", {"default": "black hair, long hair, straight hair, blue eyes, slim, school uniform, standing, looking at viewer, smiling"}),
                "character_1_type": (["girl", "boy", "elf", "demon", "maid", "magical girl", "nun", "witch"], {"default": "girl"}),
                
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
                # Character 2
                "character_2_desc": ("STRING", {"default": ""}),
                "character_2_type": (["", "girl", "boy", "elf", "demon", "maid", "magical girl", "nun", "witch"], {"default": ""}),
                
                # Character 3
                "character_3_desc": ("STRING", {"default": ""}),
                "character_3_type": (["", "girl", "boy", "elf", "demon", "maid", "magical girl", "nun", "witch"], {"default": ""}),
                
                # Character 4
                "character_4_desc": ("STRING", {"default": ""}),
                "character_4_type": (["", "girl", "boy", "elf", "demon", "maid", "magical girl", "nun", "witch"], {"default": ""}),
                
                # Character 5
                "character_5_desc": ("STRING", {"default": ""}),
                "character_5_type": (["", "girl", "boy", "elf", "demon", "maid", "magical girl", "nun", "witch"], {"default": ""}),
                
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
        character_1_desc: str,
        character_1_type: str,
        location: str,
        lighting: str,
        time_of_day: str,
        camera_angle: str,
        art_style: str,
        quality_tags: str,
        character_2_desc: str = "",
        character_2_type: str = "",
        character_3_desc: str = "",
        character_3_type: str = "",
        character_4_desc: str = "",
        character_4_type: str = "",
        character_5_desc: str = "",
        character_5_type: str = "",
        composition: str = "",
        scene_description: str = "",
        negative_prompt: str = "",
    ) -> Tuple[str, str]:
        """Generate multi-character scene prompt.
        
        Automatically counts and formats character count (1girl, 2girls, 1boy, etc)
        at the beginning of the prompt.
        
        Returns:
            Tuple of (positive_prompt, negative_prompt) as strings.
        """
        
        prompt_parts = []
        
        # Collect characters and their types
        characters = [
            (character_1_desc, character_1_type),
            (character_2_desc, character_2_type),
            (character_3_desc, character_3_type),
            (character_4_desc, character_4_type),
            (character_5_desc, character_5_type),
        ]
        
        # Count girls and boys
        girls = 0
        boys = 0
        char_descriptions = []
        
        for desc, char_type in characters:
            if desc.strip() and char_type.strip():
                if char_type.strip().lower() == "girl":
                    girls += 1
                elif char_type.strip().lower() == "boy":
                    boys += 1
                char_descriptions.append(desc)
        
        # Add character count at the beginning (Danbooru/Wailustrious standard)
        if girls > 0 or boys > 0:
            count_str = self._format_character_count(girls, boys)
            prompt_parts.append(count_str)
        
        # Add character descriptions
        for desc in char_descriptions:
            if desc.strip():
                prompt_parts.append(desc)
        
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
    
    @staticmethod
    def _format_character_count(girls: int, boys: int) -> str:
        """Format character count in Danbooru style (1girl, 2girls, 1boy, etc)."""
        parts = []
        if girls == 1:
            parts.append("1girl")
        elif girls > 1:
            parts.append(f"{girls}girls")
        
        if boys == 1:
            parts.append("1boy")
        elif boys > 1:
            parts.append(f"{boys}boys")
        
        return ", ".join(parts)

