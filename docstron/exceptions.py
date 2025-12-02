"""
Custom exceptions for the Docstron SDK
"""


class DocstronError(Exception):
    """Base exception for all Docstron errors"""

    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response


class AuthenticationError(DocstronError):
    """Raised when authentication fails"""

    pass


class NotFoundError(DocstronError):
    """Raised when a resource is not found"""

    pass


class ValidationError(DocstronError):
    """Raised when request validation fails"""

    pass


class RateLimitError(DocstronError):
    """Raised when rate limit is exceeded"""

    pass


class ServerError(DocstronError):
    """Raised when server encounters an error"""

    pass
