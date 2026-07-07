"""
<<<<<<< HEAD
signing.py
Generates HMAC-SHA256 signature for webhook payload.
=======
Generate secure HMAC Signature
>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
"""

import json
import hmac
import hashlib
<<<<<<< HEAD
from typing import Dict, Any


def generate_signature(secret: str, payload: Dict[str, Any]) -> str:
    """
    Generate HMAC-SHA256 signature.
    """

    message = json.dumps(
        payload,
        sort_keys=True
    ).encode("utf-8")

    signature = hmac.new(
        secret.encode("utf-8"),
=======
import time
import uuid


def generate_signature(secret: str, payload: dict):
    """
    Generates HMAC-SHA256 signature.
    """

    timestamp = str(int(time.time()))
    nonce = str(uuid.uuid4())

    signed_payload = {
        "timestamp": timestamp,
        "nonce": nonce,
        "data": payload
    }

    message = json.dumps(
        signed_payload,
        sort_keys=True
    ).encode()

    signature = hmac.new(
        secret.encode(),
>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
        message,
        hashlib.sha256
    ).hexdigest()

<<<<<<< HEAD
    return signature
=======
    return signature, timestamp, nonce
>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
