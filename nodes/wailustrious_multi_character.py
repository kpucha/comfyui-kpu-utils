"""KPU Wailustrious Multi-Character Prompt Generator.

Handles multiple characters with individual attributes for complex scenes.
"""
from typing import Any, Dict, Tuple


class WailustriousMultiCharacterGenerator:
    """Generate prompts with multiple characters, each with individual attributes.
    
    Perfect for scenes with 2-5 characters where each needs specific appearance.
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        return {
            "required": {
                # Main Scene Settings
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
                
                "composition": ("STRING", {"default": ""}),  # e.g., "centered composition", "rule of thirds"
                
                # CHARACTER 1
                "char1_type": ("STRING", {"default": "girl"}),
                "char1_appearance": ("STRING", {"default": "long black hair, blue eyes, school uniform"}),
                "char1_pose": ("STRING", {"default": "standing, looking at viewer"}),
                "char1_expression": ("STRING", {"default": "smiling"}),
                
                # CHARACTER 2
                "char2_type": ("STRING", {"default": ""}),
                "char2_appearance": ("STRING", {"default": ""}),
                "char2_pose": ("STRING", {"default": ""}),
                "char2_expression": ("STRING", {"default": ""}),
                
                # CHARACTER 3 (optional)
                "char3_type": ("STRING", {"default": ""}),
                "char3_appearance": ("STRING", {"default": ""}),
                "char3_pose": ("STRING", {"default": ""}),
                "char3_expression": ("STRING", {"default": ""}),
                
                # CHARACTER 4 (optional)
                "char4_type": ("STRING", {"default": ""}),
                "char4_appearance": ("STRING", {"default": ""}),
                "char4_pose": ("STRING", {"default": ""}),
                "char4_expression": ("STRING", {"default": ""}),
                
                # CHARACTER 5 (optional)
                "char5_type": ("STRING", {"default": ""}),
                "char5_appearance": ("STRING", {"default": ""}),
                "char5_pose": ("STRING", {"default": ""}),
                "char5_expression": ("STRING", {"default": ""}),
                
                # Art Quality
                "art_style": (["anime", "manga", "illustration", "pixelart"], {"default": "anime"}),
                "quality_tags": ("STRING", {"default": "high quality, masterpiece, detailed"}),
            },
            "optional": {
                "negative_prompt": ("STRING", {"default": "ugly, deformed, blurry, lowres, watermark, text, extra fingers"}),
                "scene_description": ("STRING", {"default": ""}),  # Additional scene details
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "generate"
    CATEGORY = "KPU Utils"

    def generate(
        self,
        location: str,
        lighting: str,
        time_of_day: str,
        camera_angle: str,
        composition: str,
        char1_type: str,
        char1_appearance: str,
        char1_pose: str,
        char1_expression: str,
        char2_type: str = "",
        char2_appearance: str = "",
        char2_pose: str = "",
        char2_expression: str = "",
        char3_type: str = "",
        char3_appearance: str = "",
        char3_pose: str = "",
        char3_expression: str = "",
        char4_type: str = "",
        char4_appearance: str = "",
        char4_pose: str = "",
        char4_expression: str = "",
        char5_type: str = "",
        char5_appearance: str = "",
        char5_pose: str = "",
        char5_expression: str = "",
        art_style: str = "anime",
        quality_tags: str = "high quality, masterpiece, detailed",
        negative_prompt: str = "",
        scene_description: str = "",
    ) -> Tuple[str, str]:
        """Generate multi-character prompt.
        
        Returns:
            Tuple of (positive_prompt, negative_prompt) as strings.
        """
        
        prompt_parts = []
        
        # Build character count description
        char_count = self._count_characters(char1_type, char2_type, char3_type, char4_type, char5_type)
        if char_count:
            prompt_parts.append(char_count)
        
        # Build character descriptions
        characters = [
            (char1_type, char1_appearance, char1_pose, char1_expression),
            (char2_type, char2_appearance, char2_pose, char2_expression),
            (char3_type, char3_appearance, char3_pose, char3_expression),
            (char4_type, char4_appearance, char4_pose, char4_expression),
            (char5_type, char5_appearance, char5_pose, char5_expression),
        ]
        
        for char_type, appearance, pose, expression in characters:
            if char_type.strip():
                char_desc = []
                if char_type.strip():
                    char_desc.append(char_type)
                if appearance.strip():
                    char_desc.append(appearance)
                if pose.strip():
                    char_desc.append(pose)
                if expression.strip():
                    char_desc.append(expression)
                
                if char_desc:
                    prompt_parts.append(", ".join(char_desc))
        
        # Scene composition
        if camera_angle.strip() and camera_angle != "eye level":
            prompt_parts.append(f"{camera_angle} view")
        
        if composition.strip():
            prompt_parts.append(composition)
        
        # Setting
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
    def _count_characters(char1: str, char2: str, char3: str, char4: str, char5: str) -> str:
        """Count and describe number of characters."""
        chars = [c.strip() for c in [char1, char2, char3, char4, char5] if c.strip()]
        count = len(chars)
        
        if count == 0:
            return ""
        
        # Count by gender if possible
        girls = sum(1 for c in chars if "girl" in c.lower())
        boys = sum(1 for c in chars if "boy" in c.lower())
        
        if girls > 0 and boys == 0:
            return f"{girls}girl{'s' if girls > 1 else ''}"
        elif boys > 0 and girls == 0:
            return f"{boys}boy{'s' if boys > 1 else ''}"
        elif girls > 0 and boys > 0:
            return f"{girls}girl{'s' if girls > 1 else ''}, {boys}boy{'s' if boys > 1 else ''}"
        else:
            return f"{count} character{'s' if count > 1 else ''}"
