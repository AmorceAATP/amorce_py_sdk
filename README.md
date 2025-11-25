# Nexus Python SDK (NATP)

**Official Python SDK for the Nexus Agent Transaction Protocol (NATP).**

The Nexus SDK allows any Python application, API, or Agent to become a verified node in the **Agent Economy**. It provides the cryptographic primitives (Ed25519) and the transport layer required to transact securely with AI Agents (OpenAI, Google Gemini, Apple Intelligence).

## 🚀 Features

-   **Zero-Trust Security**: Every request is cryptographically signed (Ed25519).
    
-   **Agent Identity**: Manage your agent's identity and keys securely.
    
-   **Priority Lane**: Mark critical messages (`high`, `critical`) to bypass network congestion.
    
-   **Resilience**: Automatic retry logic with exponential backoff for unstable networks (handles 503, 429, etc.).
    
-   **Developer Experience (v0.1.5)**: Zero-config identity generation via `generate_ephemeral()` for rapid testing.
    

## 📦 Installation

```
pip install nexus-py-sdk

```

_(For development from source)_

```
git clone [https://github.com/trebortGolin/nexus_py_sdk.git](https://github.com/trebortGolin/nexus_py_sdk.git)
cd nexus_py_sdk
pip install .

```

## ⚡ Quick Start

### 1. Identity Setup

An Agent is defined by its Private Key. **Never share this key.**

#### Option A: Quick Start (Ephemeral / Testing)

Generate a new identity in memory instantly. No files required.

```
from nexus import IdentityManager

# Generates a fresh Ed25519 keypair in memory (Ephemeral)
identity = IdentityManager.generate_ephemeral()

print(f"Agent Public Key: {identity.public_key_pem}")
# You can save the private key if needed:
# print(identity.private_key_pem) 

```

#### Option B: Production (Secure Storage)

Load your identity from a secure source.

```
from nexus import IdentityManager, LocalFileProvider

# Load from a local PEM file
identity = IdentityManager(LocalFileProvider("agent_key.pem"))

```

### 2. Sending a Transaction

Use the `NexusClient` to discover services and execute transactions.

```
from nexus import NexusClient, PriorityLevel

# Initialize the client
client = NexusClient(
    identity=identity,
    directory_url="[https://directory.amorce.io](https://directory.amorce.io)",
    orchestrator_url="[https://api.amorce.io](https://api.amorce.io)",
    agent_id="your-agent-uuid"
)

# Define the payload
payload = {
    "intent": "book_reservation",
    "params": {"date": "2025-10-12", "guests": 2}
}

# Execute with PRIORITY
# Options: PriorityLevel.NORMAL, .HIGH, .CRITICAL
# The client will automatically retry if the network is unstable.
response = client.transact(
    service_contract={"service_id": "srv_restaurant_01"},
    payload=payload,
    priority=PriorityLevel.HIGH 
)

print(response)

```

## 🛡️ Architecture

The SDK implements the **NATP v0.1** standard.

1.  **Envelope**: Data is wrapped in a `NexusEnvelope`, serialized canonically, and signed.
    
    -   _New in v0.1.2_: Includes a `priority` field validated strictly by regex.
        
2.  **Transport**: The envelope is sent via HTTP/2 to the Orchestrator.
    
    -   _New in v0.1.2_: Implements exponential backoff (Retry-After) for reliability.
        
3.  **Verification**: The receiver verifies the signature against the Trust Directory before processing.
    

## 🛠️ Development

### Running Tests

To ensure the SDK works in your environment (especially the new Resilience logic):

```
# Install test dependencies
pip install -r requirements.txt

# Run the real-world integration test (spawns a local server)
python3 tests/test_resilience_real.py

```

## 📄 License

This project is licensed under the MIT License.