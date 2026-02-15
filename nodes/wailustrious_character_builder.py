"""KPU Character Builder Node.

Generates individual character descriptions optimized for Wailustrious XL.
Output can be fed into Multi-Character Generator.
"""
from typing import Any, Dict, Tuple


class WailustriousCharacterBuilder:
    """Generate a single character description with all appearance and pose details.
    
    Perfect for building individual character descriptions that can be combined
    in multi-character scenes using the Multi-Character Generator.
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        return {
            "required": {
                # Character Type
                "character_type": ("STRING", {"default": "girl"}),  # e.g., "girl", "boy", "elf girl", "demon"
                
                # Appearance - Hair
                "hair_color": ("STRING", {"default": "black"}),
                "hair_length": (["short", "shoulder-length", "long", "very long"], {"default": "long"}),
                "hair_style": ("STRING", {"default": "straight"}),  # e.g., "twintails", "wavy"
                
                # Appearance - Eyes
                "eye_color": ("STRING", {"default": "blue"}),
                "eye_shape": ("STRING", {"default": ""}),  # e.g., "cat eyes", "large eyes"
                
                # Appearance - Body
                "body_type": ("STRING", {"default": "slim"}),
                "body_feature": ("STRING", {"default": ""}),  # Optional additional features
                
                # Clothing & Accessories
                "clothing": ("STRING", {"default": "school uniform"}),
                "clothing_color": ("STRING", {"default": ""}),
                "accessories": ("STRING", {"default": ""}),
                
                # Pose & Expression
                "pose": ("STRING", {"default": "standing"}),
                "action": ("STRING", {"default": "looking at viewer"}),
                "expression": ("STRING", {"default": "smiling"}),
            },
            "optional": {
                "special_traits": ("STRING", {"default": ""}),  # e.g., "blushing", "sweating"
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("character_description",)
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
    ) -> Tuple[str]:
        """Build a single character description.
        
        Returns:
            Tuple containing the character description string.
        """
        
        parts = []
        
        # Character type (required)
        if character_type.strip():
            parts.append(character_type)
        
        # Hair
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
            parts.append(", ".join(hair_parts))
        
        # Eyes
        eye_parts = []
        if eye_color.strip():
            eye_parts.append(f"{eye_color} eyes")
        if eye_shape.strip():
            eye_parts.append(eye_shape)
        
        if eye_parts:
            parts.append(", ".join(eye_parts))
        
        # Body
        if body_type.strip():
            parts.append(body_type)
        if body_feature.strip():
            parts.append(body_feature)
        
        # Clothing
        clothing_parts = []
        if clothing.strip():
            clothing_parts.append(clothing)
        if clothing_color.strip():
            # Avoid duplication if color is in clothing name
            if clothing_color.lower() not in clothing.lower():
                clothing_parts.insert(0, clothing_color)
        
        if clothing_parts:
            parts.append(", ".join(clothing_parts))
        
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
        
        # Special traits
        if special_traits.strip():
            parts.append(special_traits)
        
        # Join all parts
        description = ", ".join(part.strip() for part in parts if part.strip())
        
        return (description,)
