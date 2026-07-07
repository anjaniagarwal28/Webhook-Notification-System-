import requests
from signing import generate_signature


def dispatch_webhook(subscriber, event, payload):
    signature = generate_signature(
        subscriber["secret"],
        payload
    )

    headers = {
        "Content-Type": "application/json",
        "X-Signature": signature
    }

    max_retries = 3

    for attempt in range(max_retries):

        try:
            response = requests.post(
                subscriber["url"],
                json=payload,
                headers=headers,
                timeout=5
            )

            response.raise_for_status()

            return {
                "webhook_id": subscriber["webhook_id"],
                "event": event,
                "status_code": response.status_code,
                "delivery_status": "Success",
                "signature": signature
            }

        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")

        except requests.exceptions.ConnectionError:
            print(f"Connection error on attempt {attempt + 1}")

        except requests.exceptions.HTTPError:
            print(f"HTTP error on attempt {attempt + 1}")

    return {
        "webhook_id": subscriber["webhook_id"],
        "event": event,
        "delivery_status": "Failed after retries"
    }
