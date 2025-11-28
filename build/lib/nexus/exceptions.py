"""
Nexus Exceptions Module
Defines custom exceptions for the Nexus SDK to allow fine-grained error handling.
"""

class NexusError(Exception):
    """Base class for all Nexus SDK exceptions."""
    pass

class NexusConfigError(NexusError):
    """Raised when there is a configuration issue (e.g. invalid URL, missing key)."""
    pass

class NexusNetworkError(NexusError):
    """Raised when a network operation fails (e.g. connection timeout, DNS error)."""
    pass

class NexusAPIError(NexusError):
    """Raised when the Nexus API returns an error response (4xx, 5xx)."""
    def __init__(self, message: str, status_code: int = None, response_body: str = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body

class NexusSecurityError(NexusError):
    """Raised when a security-related operation fails (e.g. signing, key loading)."""
    pass

class NexusValidationError(NexusError):
    """Raised when data validation fails (e.g. invalid envelope structure)."""
    pass
