import requests
import json
import hmac
import hashlib

# -----------------------------
# Subscriber Data
# -----------------------------
subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",   # Test webhook URL
        "secret": "mysecretkey"
    }
]

# -----------------------------
# Event Data
# -----------------------------
event_data = {
    "event": "interview.booked",
    "candidate": "John Doe",
    "date": "2026-07-01",
    "time": "10:00 AM"
}

# -----------------------------
# Send Webhook Function
# -----------------------------
def send_webhook(subscriber, payload):

    # Convert payload to JSON
    payload_json = json.dumps(payload)

    # Generate HMAC Signature
    signature = hmac.new(
        subscriber["secret"].encode(),
        payload_json.encode(),
        hashlib.sha256
    ).hexdigest()

    # HTTP Headers
    headers = {
        "Content-Type": "application/json",
        "X-Webhook-Signature": signature
    }

    try:
        response = requests.post(
            subscriber["url"],
            data=payload_json,
            headers=headers,
            timeout=5
        )

        result = {
            "webhook_id": subscriber["webhook_id"],
            "event": payload["event"],
            "delivery_status": f"{response.status_code} {response.reason}"
        }

    except Exception:
        result = {
            "webhook_id": subscriber["webhook_id"],
            "event": payload["event"],
            "delivery_status": "Delivery Failed"
        }

    return result


# -----------------------------
# Main Program
# -----------------------------
for subscriber in subscribers:
    output = send_webhook(subscriber, event_data)
    print(output)