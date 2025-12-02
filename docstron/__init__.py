"""
Docstron Python SDK

A Python SDK for the Docstron PDF Generation API.
"""

from .client import Docstron
from .exceptions import (
    DocstronError,
    AuthenticationError,
    NotFoundError,
    ValidationError,
    RateLimitError,
)

__version__ = "1.0.0"
__all__ = [
    "Docstron",
    "DocstronError",
    "AuthenticationError",
    "NotFoundError",
    "ValidationError",
    "RateLimitError",
]
