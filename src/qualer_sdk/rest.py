"""
REST module compatibility layer for legacy test imports.

This module provides compatibility for the old Java-based OpenAPI generator
that used to generate a `rest` module. We map it to the new errors module.
"""

# Import exceptions from the new errors module for backward compatibility
from .errors import UnexpectedStatus as ApiException

# Re-export for backward compatibility
__all__ = [
    "ApiException",
]
