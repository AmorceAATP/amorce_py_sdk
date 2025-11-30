"""
Amorce Exceptions Module
Defines custom exceptions for the Amorce SDK to allow fine-grained error handling.
"""

class AmorceError(Exception):
    """Base class for all Amorce SDK exceptions."""
    pass

class AmorceConfigError(AmorceError):
    """Raised when there is a configuration issue (e.g. invalid URL, missing key)."""
    pass

class AmorceNetworkError(AmorceError):
    """Raised when a network operation fails (e.g. connection timeout, DNS error)."""
    pass

class AmorceAPIError(AmorceError):
    """Raised when the Amorce API returns an error response (4xx, 5xx)."""
    def __init__(self, message: str, status_code: int = None, response_body: str = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body

class AmorceSecurityError(AmorceError):
    """Raised when a security-related operation fails (e.g. signing, key loading)."""
    pass

class AmorceValidationError(AmorceError):
    """Raised when data validation fails (e.g. invalid envelope structure)."""
    pass
