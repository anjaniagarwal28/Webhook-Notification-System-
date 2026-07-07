import json
import hmac
import hashlib

# ---------------------------------
# Webhook Notification System
# ---------------------------------

# Store webhook subscriber details
subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://example.com/webhook",
        "secret": "my_secret_key"
    }
]

# Event to be sent
event = "interview.booked"

# Payload
payload = {
    "candidate": "Rahul Sharma",
    "position": "Software Developer",
    "date": "03-07-2026"
}

# Function to generate HMAC signature
def generate_signature(secret, payload):
    message = json.dumps(payload).encode()
    signature = hmac.new(
        secret.encode(),
        message,
        hashlib.sha256
    ).hexdigest()
    return signature

# Function to simulate webhook delivery
def dispatch_webhook(subscriber, event, payload):
    signature = generate_signature(subscriber["secret"], payload)

    # Simulate successful delivery
    delivery_status = "200 OK"

    result = {
        "webhook_id": subscriber["webhook_id"],
        "event": event,
        "delivery_status": delivery_status
    }

    return result

# Send webhook to all subscribers
for subscriber in subscribers:
    output = dispatch_webhook(subscriber, event, payload)
    print(json.dumps(output, indent=4))
