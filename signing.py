"""
signing.py
Generates HMAC-SHA256 signature for webhook payload.
"""

import json
import hmac
import hashlib
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
        message,
        hashlib.sha256
    ).hexdigest()

    return signature
