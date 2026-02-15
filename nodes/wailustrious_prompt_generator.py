"""KPU Wailustrious Prompt Generator Node.

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
                
                # Appearance - Hair
                "hair_color": ("STRING", {"default": "black"}),
                "hair_length": (["short", "shoulder-length", "long", "very long"], {"default": "long"}),
                "hair_style": ("STRING", {"default": "straight"}),  # e.g., "twintails", "wavy", "curly"
                
                # Appearance - Eyes
                "eye_color": ("STRING", {"default": "blue"}),
                "eye_shape": ("STRING", {"default": ""}),  # e.g., "cat eyes", "large eyes"
                
                # Appearance - Body
                "body_type": ("STRING", {"default": "slim"}),  # e.g., "slim", "curvy", "muscular"
                "body_feature": ("STRING", {"default": ""}),  # Optional additional body features
                
                # Clothing
                "clothing": ("STRING", {"default": "school uniform"}),
                "clothing_color": ("STRING", {"default": ""}),
                "accessories": ("STRING", {"default": ""}),
                
                # Pose & Action
                "pose": ("STRING", {"default": "standing"}),
                "action": ("STRING", {"default": "looking at viewer"}),
                "expression": ("STRING", {"default": "smiling"}),
                
                # Camera & Composition
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
                "composition": ("STRING", {"default": ""}),  # e.g., "centered", "rule of thirds"
                
                # Setting
                "location": ("STRING", {"default": "bedroom"}),
                "lighting": ("STRING", {"default": "soft lighting"}),
                "time_of_day": ("STRING", {"default": "daytime"}),
                "background_detail": ("STRING", {"default": ""}),
                
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
        hair_color: str,
        hair_length: str,
        hair_style: str,
        eye_color: str,
        eye_shape: str,
        body_type: str,
        body_feature: str,
        clothing: str,
        clothing_color: str,
        accessories: str,
        pose: str,
        action: str,
        expression: str,
        camera_angle: str,
        composition: str,
        location: str,
        lighting: str,
        time_of_day: str,
        background_detail: str,
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
        
        # 2. Appearance - Hair
        hair_parts = []
        if hair_color.strip() and hair_color.lower() != "black":
            hair_parts.append(f"{hair_color} hair")
        elif hair_color.strip():
            hair_parts.append("black hair")
        
        if hair_length.strip():
            hair_parts.append(hair_length)
        
        if hair_style.strip():
            hair_parts.append(f"{hair_style} hair")
        
        if hair_parts:
            prompt_parts.append(", ".join(hair_parts))
        
        # 3. Appearance - Eyes
        eye_parts = []
        if eye_color.strip():
            eye_parts.append(f"{eye_color} eyes")
        
        if eye_shape.strip():
            eye_parts.append(eye_shape)
        
        if eye_parts:
            prompt_parts.append(", ".join(eye_parts))
        
        # 4. Appearance - Body
        if body_type.strip():
            prompt_parts.append(body_type)
        
        if body_feature.strip():
            prompt_parts.append(body_feature)
        
        # 5. Clothing
        clothing_parts = []
        if clothing.strip():
            clothing_parts.append(clothing)
        if clothing_color.strip():
            clothing_parts.append(f"{clothing_color} {clothing}".strip())
        if clothing_parts:
            prompt_parts.append(", ".join(clothing_parts))
        
        if accessories.strip():
            prompt_parts.append(accessories)
        
        # 6. Pose & Action
        if pose.strip():
            prompt_parts.append(pose)
        if action.strip():
            prompt_parts.append(action)
        if expression.strip():
            prompt_parts.append(expression)
        
        # 7. Camera & Composition
        if camera_angle.strip() and camera_angle != "eye level":
            prompt_parts.append(f"{camera_angle} view")
        
        if composition.strip():
            prompt_parts.append(composition)
        
        # 8. Setting
        if location.strip():
            prompt_parts.append(location)
        if background_detail.strip():
            prompt_parts.append(background_detail)
        if lighting.strip():
            prompt_parts.append(lighting)
        if time_of_day.strip():
            prompt_parts.append(time_of_day)
        
        # 9. Art Style
        prompt_parts.append(art_style)
        if quality_tags.strip():
            prompt_parts.append(quality_tags)
        
        # 10. Custom tags
        if custom_tags.strip():
            prompt_parts.append(custom_tags)
        
        # 11. Weight emphasis (optional)
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

    def build(self, preset: str, camera_angle: str = "eye level", modify: str = "") -> Tuple[str, ...]:
        """Build prompt from preset with camera angle and optional modifications.
        
        Args:
            preset: Name of preset configuration
            camera_angle: Camera angle/composition
            modify: Additional tags to append (comma-separated)
        
        Returns:
            Tuple containing the generated prompt
        """
        base_prompt = self.PRESETS.get(preset, self.PRESETS["casual"])
        
        # Add camera angle if not default
        prompt_parts = [base_prompt]
        if camera_angle.strip() and camera_angle != "eye level":
            prompt_parts.append(f"{camera_angle} view")
        
        # Add custom modifications
        if modify.strip():
            prompt_parts.append(modify)
        
        prompt = ", ".join(prompt_parts)
        
        return (prompt,)
