"""Small helper utilities used by KPU nodes.

Keep these helpers minimal and dependency-free where possible.
"""
from typing import Any


def dummy_process(image: Any) -> Any:
    """A trivial helper that currently performs a no-op on `image`.

    Replace this with real preprocessing/postprocessing helpers as needed.
    """
    return image
