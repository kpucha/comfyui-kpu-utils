"""KPU Scene Generator Node

Generates scene prompts based on numeric input for dynamic text fields."""

from typing import Any, Dict, Tuple


class KPUSceneGenerator:
    """Generates scene prompts based on numeric input for dynamic text fields."""

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        return {
            "required": {
                "num_textos": ("INT", {"default": 1, "min": 0, "max": 3}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "execute"
    CATEGORY = "KPU Utils"

    @classmethod
    def get_input_types(cls, inputs: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """Dinamically generate optional fields based on num_textos value."""
        if "num_textos" in inputs:
            num = inputs["num_textos"]
            optional = {}
            for i in range(1, num + 1):
                optional[f"texto_{i}"] = ("STRING", {"default": ""})
            return {"required": {}, "optional": optional}
        return {"required": {}, "optional": {}}

    def execute(
        self,
        num_textos: int,
        **kwargs: Dict[str, Any]
    ) -> Tuple[str, str]:
        """Generate scene prompt based on numeric input."""
        textos = []
        for i in range(1, num_textos + 1):
            texto = kwargs.get(f"texto_{i}", "")
            if texto:
                textos.append(texto)
        return ("\n".join(textos), "ugly, deformed, blurry, lowres, watermark, text, extra fingers")
