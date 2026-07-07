import json
import hmac
import hashlib


def generate_signature(secret, payload):
    message = json.dumps(
        payload,
        sort_keys=True
    ).encode()

    return hmac.new(
        secret.encode(),
        message,
        hashlib.sha256
    ).hexdigest()
