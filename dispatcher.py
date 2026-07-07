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
        signature, timestamp, nonce = generate_signature(
            subscriber["secret"],
            payload
        )

        body = {
            "event": event,
            "timestamp": timestamp,
            "nonce": nonce,
            "payload": payload
        }

        headers = {
            "Content-Type": "application/json",
            "X-Webhook-Signature": signature
        }

        retries = 3

        for attempt in range(1, retries + 1):

            try:
                response = requests.post(
                    subscriber["url"],
                    json=body,
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
                print(f"Timeout on attempt {attempt}")

            except requests.exceptions.ConnectionError:
                print(f"Connection Error on attempt {attempt}")

            except requests.exceptions.HTTPError:
                print(f"HTTP Error on attempt {attempt}")

            except requests.exceptions.RequestException:
                print(f"Request Error on attempt {attempt}")

            time.sleep(2 ** (attempt - 1))

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
        
