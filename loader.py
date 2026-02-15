"""Loader for comfyui-kpu-utils nodes.

Expose `register_nodes()` which returns a list of node classes that a
host application (or test harness) can import and register.
"""
from nodes import KPUExampleNode


def register_nodes():
    """Return list of node classes provided by this package."""
    return [KPUExampleNode]
