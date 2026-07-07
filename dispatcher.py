"""
<<<<<<< HEAD
dispatcher.py
Dispatches webhook requests.
"""

import time
=======
Dispatch Webhooks
"""

>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
import requests

from signing import generate_signature


<<<<<<< HEAD
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
=======
def dispatch_webhook(subscriber: dict,
                     event: str,
                     payload: dict) -> dict:
    """
    Sends webhook with retry mechanism.
    """

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

    return {
        "webhook_id": subscriber["webhook_id"],
        "event": event,
        "delivery_status": "Failed after retries"
    }
>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
