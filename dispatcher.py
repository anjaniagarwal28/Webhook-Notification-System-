"""
dispatcher.py
Dispatches webhook requests.
"""

import time
import requests

from signing import generate_signature


def dispatch_webhook(subscriber, event, payload):
    """
    Send webhook with retry mechanism.
    """

    try:

        signature = generate_signature(
            subscriber["secret"],
            payload
        )

        headers = {
            "Content-Type": "application/json",
            "X-Webhook-Event": event,
            "X-Webhook-Signature": signature,
            "X-Webhook-Timestamp": str(payload["timestamp"])
        }

        retries = 3

        for attempt in range(retries):

            try:

                response = requests.post(
                    subscriber["url"],
                    json=payload,
                    headers=headers,
                    timeout=5
                )

                if response.status_code in [200, 201, 202]:

                    return {
                        "webhook_id": subscriber["webhook_id"],
                        "event": event,
                        "status_code": response.status_code,
                        "delivery_status": "Success",
                        "signature": signature
                    }

                else:

                    print(
                        f"Attempt {attempt+1} failed "
                        f"({response.status_code})"
                    )

            except requests.exceptions.RequestException:

                print(
                    f"Network error on attempt {attempt+1}"
                )

            time.sleep(2 ** attempt)

        return {
            "webhook_id": subscriber["webhook_id"],
            "event": event,
            "delivery_status": "Failed after retries"
        }

    except KeyError as e:

        return {
            "error": f"Missing field: {e}"
        }

    except Exception as e:

        return {
            "error": str(e)
        }