# Nexus SDK Core
# Version 0.1.7

__version__ = "0.1.7"

# Task 1: Crypto & Identity
from .crypto import IdentityManager, LocalFileProvider, EnvVarProvider, GoogleSecretManagerProvider

# Task 2: Protocol Envelope
# DX FIX: Aliasing NexusEnvelope to Envelope for simpler imports
from .envelope import NexusEnvelope, NexusEnvelope as Envelope, PriorityLevel

# Task 3: Client
from .client import NexusClient

# Task 4: Exceptions
from .exceptions import (
    NexusError,
    NexusConfigError,
    NexusNetworkError,
    NexusAPIError,
    NexusSecurityError,
    NexusValidationError
)

# Flattening exports as requested by QA Ticket
__all__ = [
    "NexusClient",
    "NexusEnvelope",
    "Envelope",
    "PriorityLevel",
    "IdentityManager",
    "LocalFileProvider",
    "EnvVarProvider",
    "EnvVarProvider",
    "GoogleSecretManagerProvider",
    "NexusError",
    "NexusConfigError",
    "NexusNetworkError",
    "NexusAPIError",
    "NexusSecurityError",
    "NexusValidationError"
]