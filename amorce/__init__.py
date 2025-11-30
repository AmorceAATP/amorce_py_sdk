# Amorce SDK Core
# Version 0.1.7

__version__ = "0.1.7"

# Task 1: Crypto & Identity
from .crypto import IdentityManager, LocalFileProvider, EnvVarProvider, GoogleSecretManagerProvider

# Task 2: Protocol Envelope
# DX FIX: Aliasing AmorceEnvelope to Envelope for simpler imports
from .envelope import AmorceEnvelope, AmorceEnvelope as Envelope, PriorityLevel

# Task 3: Client
from .client import AmorceClient

# Task 4: Exceptions
from .exceptions import (
    AmorceError,
    AmorceConfigError,
    AmorceNetworkError,
    AmorceAPIError,
    AmorceSecurityError,
    AmorceValidationError
)

# Flattening exports as requested by QA Ticket
__all__ = [
    "AmorceClient",
    "AmorceEnvelope",
    "Envelope",
    "PriorityLevel",
    "IdentityManager",
    "LocalFileProvider",
    "EnvVarProvider",
    "EnvVarProvider",
    "GoogleSecretManagerProvider",
    "AmorceError",
    "AmorceConfigError",
    "AmorceNetworkError",
    "AmorceAPIError",
    "AmorceSecurityError",
    "AmorceValidationError"
]