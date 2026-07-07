"""
app.py
Main entry point for Webhook Notification System.
"""

import json
import time

from config import subscribers
from dispatcher import dispatch_webhook


def main():
    event = "interview.booked"

    payload = {
        "candidate": "Rahul Sharma",
        "position": "Software Developer",
        "date": "03-07-2026",
        "timestamp": int(time.time())
    }

    if not subscribers:
        print("No subscribers found.")
        return

    print("=" * 60)
    print("WEBHOOK NOTIFICATION SYSTEM")
    print("=" * 60)

    for subscriber in subscribers:
        result = dispatch_webhook(
            subscriber,
            event,
            payload
        )

        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
