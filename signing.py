"""
Generate secure HMAC Signature
"""

import json
import hmac
import hashlib
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
        message,
        hashlib.sha256
    ).hexdigest()

    return signature, timestamp, nonce
