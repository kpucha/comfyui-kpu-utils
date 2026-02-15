"""KPU Character Builder Node.

Generates individual character descriptions optimized for Wailustrious XL.
Uses Danbooru tag format for compatibility and consistency.
"""
from typing import Any, Dict, Tuple


class WailustriousCharacterBuilder:
    """Generate a single character description with Danbooru tags.
    
    Returns character_type separately so Multi-Character Scene can count girls/boys.
    Character count (1girl, 1boy, etc) is NOT included here - handled by Multi-Character Scene.
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        return {
            "required": {
                # Character Type (gender - returned separately for counting)
                "character_type": (["girl", "boy", "elf", "demon", "maid", "magical girl", "nun", "witch"], {"default": "girl"}),
                
                # Appearance - Hair (Danbooru tags)
                "hair_color": (
                    ["black", "white", "brown", "red", "pink", "purple", "blue", "green", "yellow", "orange", "grey", "silver", "blonde", "cyan"],
                    {"default": "black"},
                ),
                "hair_length": (["very short hair", "short hair", "shoulder-length hair", "long hair", "very long hair"], {"default": "long hair"}),
                "hair_style": (
                    ["straight hair", "wavy hair", "curly hair", "twintails", "drill hair", "side ponytail", "ponytail", "hime cut", "braid"],
                    {"default": "straight hair"},
                ),
                
                # Appearance - Eyes
                "eye_color": (
                    ["black eyes", "white eyes", "brown eyes", "red eyes", "pink eyes", "purple eyes", "blue eyes", "green eyes", "yellow eyes", "orange eyes", "grey eyes", "cyan eyes"],
                    {"default": "blue eyes"},
                ),
                "eye_shape": (
                    ["", "large eyes", "small eyes", "cat eyes", "fox eyes", "sharp eyes"],
                    {"default": ""},
                ),
                
                # Appearance - Body
                "body_type": (["slim", "slender", "petite", "curvy", "busty", "muscular", "athletic"], {"default": "slim"}),
                "body_feature": ("STRING", {"default": ""}),  # e.g., "breasts" (Danbooru compatible)
                
                # Clothing & Accessories (Danbooru tags)
                "clothing": (
                    ["school uniform", "sailor uniform", "maid outfit", "dress", "casual clothes", "formal suit", "fantasy outfit", "armor", "kimono", "bikini", "sportswear"],
                    {"default": "school uniform"},
                ),
                "clothing_color": (
                    ["", "white", "black", "blue", "red", "green", "purple", "pink", "yellow", "brown"],
                    {"default": ""},
                ),
                "accessories": ("STRING", {"default": ""}),  # e.g., "glasses", "tiara", "ribbon"
                
                # Pose & Expression
                "pose": (
                    ["standing", "sitting", "lying down", "kneeling", "floating", "jumping", "running", "dancing"],
                    {"default": "standing"},
                ),
                "action": (
                    ["looking at viewer", "looking away", "profile", "back view", "from above", "from below"],
                    {"default": "looking at viewer"},
                ),
                "expression": (
                    ["smiling", "happy", "neutral", "serious", "sad", "embarrassed", "blushing", "closed eyes"],
                    {"default": "smiling"},
                ),
            },
            "optional": {
                "special_traits": ("STRING", {"default": ""}),  # Custom Danbooru tags
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("character_description", "character_type")
    FUNCTION = "build"
    CATEGORY = "KPU Utils"

    def build(
        self,
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
        special_traits: str = "",
    ) -> Tuple[str, str]:
        """Build a single character description.
        
        Returns:
            Tuple of (character_description, character_type).
            Character type is returned separately so Multi-Character Scene can count them.
        """
        
        parts = []
        
        # Hair - color + length + style (avoid duplication with "hair" suffix)
        if hair_color.strip():
            parts.append(f"{hair_color} hair")
        
        if hair_length.strip() and "hair" not in hair_length:
            parts.append(hair_length)
        elif hair_length.strip():
            parts.append(hair_length)
        
        if hair_style.strip() and "hair" not in hair_style:
            parts.append(hair_style)
        elif hair_style.strip():
            parts.append(hair_style)
        
        # Eyes
        if eye_color.strip():
            parts.append(eye_color)
        if eye_shape.strip():
            parts.append(eye_shape)
        
        # Body
        if body_type.strip():
            parts.append(body_type)
        if body_feature.strip():
            parts.append(body_feature)
        
        # Clothing
        if clothing.strip():
            parts.append(clothing)
        if clothing_color.strip():
            parts.append(clothing_color)
        
        # Accessories
        if accessories.strip():
            parts.append(accessories)
        
        # Pose & Expression
        if pose.strip():
            parts.append(pose)
        if action.strip():
            parts.append(action)
        if expression.strip():
            parts.append(expression)
        
        # Special traits (custom tags)
        if special_traits.strip():
            parts.append(special_traits)
        
        # Join all parts
        description = ", ".join(part.strip() for part in parts if part.strip())
        
        # Return description and character type separately
        return (description, character_type)
