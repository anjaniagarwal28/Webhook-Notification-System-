"""
signing.py
Generates HMAC-SHA256 signature for webhook payload.
"""

import json
import hmac
import hashlib
import time
import uuid


def generate_signature(secret: str, payload: dict):
    """
    Generate HMAC-SHA256 signature with timestamp and nonce.
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
    ).encode("utf-8")

    signature = hmac.new(
        secret.encode("utf-8"),
        message,
        hashlib.sha256
    ).hexdigest()

    return signature, timestamp, nonce
