"""Wailustrious XL Prompt Generator Node.

A ComfyUI node designed to generate well-structured prompts
optimized for Wailustrious XL model following best practices.
"""
from typing import Any, Dict, Tuple


class WailustriousPromptGenerator:
    """Generate structured prompts for Wailustrious XL anime model.
    
    Combines character, appearance, pose, setting, and style information
    into a cohesive positive prompt with optional negative prompt.
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        return {
            "required": {
                # Characters
                "character_count": (["1girl", "1boy", "2girls", "2boys", "1girl, 1boy", "3girls", "3boys", "5girls", "group"],),
                "character_type": ("STRING", {"default": ""}),  # e.g., "elf, demon girl, maid"
                
                # Appearance
                "hair": ("STRING", {"default": "long black hair"}),
                "eyes": ("STRING", {"default": "blue eyes"}),
                "body_type": ("STRING", {"default": "slim"}),
                "clothing": ("STRING", {"default": "school uniform"}),
                "accessories": ("STRING", {"default": ""}),
                
                # Pose & Action
                "pose": ("STRING", {"default": "standing"}),
                "action": ("STRING", {"default": "looking at viewer"}),
                "expression": ("STRING", {"default": "smiling"}),
                
                # Setting
                "location": ("STRING", {"default": "bedroom"}),
                "lighting": ("STRING", {"default": "soft lighting"}),
                "time_of_day": ("STRING", {"default": "daytime"}),
                
                # Art Quality
                "art_style": (["anime", "manga", "illustration", "pixelart"], {"default": "anime"}),
                "quality_tags": ("STRING", {"default": "high quality, masterpiece, detailed"}),
            },
            "optional": {
                "negative_prompt": ("STRING", {"default": "ugly, deformed, blurry, lowres, watermark, text, extra fingers"}),
                "custom_tags": ("STRING", {"default": ""}),  # Additional custom tags
                "weight_emphasis": ("STRING", {"default": ""}),  # e.g., "(very beautiful:1.5)"
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "generate"
    CATEGORY = "KPU Utils"

    def generate(
        self,
        character_count: str,
        character_type: str,
        hair: str,
        eyes: str,
        body_type: str,
        clothing: str,
        accessories: str,
        pose: str,
        action: str,
        expression: str,
        location: str,
        lighting: str,
        time_of_day: str,
        art_style: str,
        quality_tags: str,
        negative_prompt: str = "",
        custom_tags: str = "",
        weight_emphasis: str = "",
    ) -> Tuple[str, str]:
        """Generate positive and negative prompts for Wailustrious XL.
        
        Returns:
            Tuple of (positive_prompt, negative_prompt) as strings.
        """
        
        # Build positive prompt in order of importance
        prompt_parts = []
        
        # 1. Characters (CRITICAL - goes first)
        prompt_parts.append(character_count)
        if character_type.strip():
            prompt_parts.append(character_type)
        
        # 2. Appearance
        if hair.strip():
            prompt_parts.append(hair)
        if eyes.strip():
            prompt_parts.append(eyes)
        if body_type.strip():
            prompt_parts.append(body_type)
        if clothing.strip():
            prompt_parts.append(clothing)
        if accessories.strip():
            prompt_parts.append(accessories)
        
        # 3. Pose & Action
        if pose.strip():
            prompt_parts.append(pose)
        if action.strip():
            prompt_parts.append(action)
        if expression.strip():
            prompt_parts.append(expression)
        
        # 4. Setting
        if location.strip():
            prompt_parts.append(location)
        if lighting.strip():
            prompt_parts.append(lighting)
        if time_of_day.strip():
            prompt_parts.append(time_of_day)
        
        # 5. Art Style
        prompt_parts.append(art_style)
        if quality_tags.strip():
            prompt_parts.append(quality_tags)
        
        # 6. Custom tags
        if custom_tags.strip():
            prompt_parts.append(custom_tags)
        
        # 7. Weight emphasis (optional)
        if weight_emphasis.strip():
            prompt_parts.append(weight_emphasis)
        
        # Join all parts
        positive_prompt = ", ".join(part.strip() for part in prompt_parts if part.strip())
        
        # Ensure negative prompt is not empty
        if not negative_prompt.strip():
            negative_prompt = "ugly, deformed, blurry, lowres, watermark, text, extra fingers"
        
        return (positive_prompt, negative_prompt)


class WailustriousPromptBuilder:
    """Advanced prompt builder with preset combinations for Wailustrious XL."""

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        presets = {
            "schoolgirl": "1girl, school uniform, short skirt, white socks, long black hair, blue eyes, standing, looking at viewer, smiling, classroom, sunlight, daytime",
            "maid": "1girl, maid outfit, maid headband, black hair, red eyes, standing, bowing slightly, embarrassed blush, mansion interior, warm lighting",
            "elf": "1girl, elf, pointed ears, long silver hair, green eyes, fantasy dress, forest, magical lighting, night",
            "demon": "1girl, demon, horns, red skin, devil tail, seductive pose, looking at viewer, underworld, red lighting",
            "angel": "1girl, angel, white wings, halo, long white hair, blue eyes, heavenly light, clouds, peaceful expression",
            "casual": "1girl, casual clothes, jeans, t-shirt, sneakers, relaxed pose, comfortable expression, bedroom, warm lighting",
            "formal": "1girl, formal dress, elegant, sophisticated, ballroom, dramatic lighting, confident expression",
            "fantasy": "1girl, fantasy warrior, armor, sword, epic pose, dramatic lighting, castle background, heroic expression",
        }

        return {
            "required": {
                "preset": (list(presets.keys()),),
                "modify": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build"
    CATEGORY = "KPU Utils"

    PRESETS = {
        "schoolgirl": "1girl, school uniform, short skirt, white socks, long black hair, blue eyes, standing, looking at viewer, smiling, classroom, sunlight, daytime, high quality, masterpiece, anime illustration",
        "maid": "1girl, maid outfit, maid headband, black hair, red eyes, standing, bowing slightly, embarrassed blush, mansion interior, warm lighting, high quality, masterpiece, anime illustration",
        "elf": "1girl, elf, pointed ears, long silver hair, green eyes, fantasy dress, forest, magical lighting, night, high quality, masterpiece, anime illustration",
        "demon": "1girl, demon, horns, red skin, devil tail, seductive pose, looking at viewer, underworld, red lighting, high quality, masterpiece, anime illustration",
        "angel": "1girl, angel, white wings, halo, long white hair, blue eyes, heavenly light, clouds, peaceful expression, high quality, masterpiece, anime illustration",
        "casual": "1girl, casual clothes, jeans, t-shirt, sneakers, relaxed pose, comfortable expression, bedroom, warm lighting, high quality, masterpiece, anime illustration",
        "formal": "1girl, formal dress, elegant, sophisticated, ballroom, dramatic lighting, confident expression, high quality, masterpiece, anime illustration",
        "fantasy": "1girl, fantasy warrior, armor, sword, epic pose, dramatic lighting, castle background, heroic expression, high quality, masterpiece, anime illustration",
    }

    def build(self, preset: str, modify: str = "") -> Tuple[str, ...]:
        """Build prompt from preset, optionally modified.
        
        Args:
            preset: Name of preset configuration
            modify: Additional tags to append (comma-separated)
        
        Returns:
            Tuple containing the generated prompt
        """
        base_prompt = self.PRESETS.get(preset, self.PRESETS["casual"])
        
        if modify.strip():
            prompt = f"{base_prompt}, {modify}"
        else:
            prompt = base_prompt
        
        return (prompt,)
