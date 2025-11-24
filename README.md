# Nexus Python SDK (NATP)

[![PyPI version](https://badge.fury.io/py/nexus-py-sdk.svg)](https://badge.fury.io/py/nexus-py-sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Official Python SDK for the Nexus Agent Transaction Protocol (NATP).**

The Nexus SDK allows any Python application, API, or Agent to become a verified node in the **Agent Economy**. It provides the cryptographic primitives (Ed25519) and the transport layer required to transact securely with AI Agents (OpenAI, Google Gemini, Apple Intelligence).

---

## 🚀 Features

* **Zero-Trust Security**: Every request is cryptographically signed (Ed25519).
* **Agent Identity**: Manage your agent's identity and keys securely.
* **Priority Lane**: Mark critical messages (`high`, `critical`) to bypass network congestion.
* **Resilience**: Automatic retry logic with exponential backoff for unstable networks (handles 503, 429, etc.).
* **Developer Experience (v0.1.3)**: Simplified imports and explicit dependencies.

---

## 📦 Installation

```bash
pip install nexus-py-sdk
(For development from source)

Bash

git clone [https://github.com/trebortGolin/nexus_py_sdk.git](https://github.com/trebortGolin/nexus_py_sdk.git)
cd nexus_py_sdk
pip install .
⚡ Quick Start
1. Identity Setup
An Agent is defined by its Private Key. Never share this key.

Python

# v0.1.3: Direct import from root package
from nexus import IdentityManager, LocalFileProvider

# Load your identity from a local PEM file
identity = IdentityManager(LocalFileProvider("agent_key.pem"))

print(f"Agent Public Key: {identity.public_key_pem}")
2. Sending a Transaction
Use the NexusClient to discover services and execute transactions.

Python

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
response = client.transact(
    service_contract={"service_id": "srv_restaurant_01"},
    payload=payload,
    priority=PriorityLevel.HIGH 
)

print(response)
🛡️ Architecture
The SDK implements the NATP v0.1 standard.

Envelope: Data is wrapped in a NexusEnvelope, serialized canonically, and signed.

Transport: The envelope is sent via HTTP/2 to the Orchestrator with automatic retries.

Verification: The receiver verifies the signature against the Trust Directory before processing.

🛠️ Development
Running Tests
To ensure the SDK works in your environment:

Bash

# Install test dependencies
pip install -r requirements.txt

# Run the integration test
python3 tests/test_resilience_real.py
📄 License
This project is licensed under the MIT License.