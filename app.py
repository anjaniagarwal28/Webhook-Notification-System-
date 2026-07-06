"""
Main entry point for Webhook Notification System
"""

import json
from config import subscribers
from dispatcher import dispatch_webhook


def main():
    event = "interview.booked"

    payload = {
        "candidate": "Rahul Sharma",
        "position": "Software Developer",
        "date": "03-07-2026"
    }

    print("=" * 60)
    print("WEBHOOK NOTIFICATION SYSTEM")
    print("=" * 60)

    if not subscribers:
        print("No subscribers found.")
        return

    for subscriber in subscribers:
        result = dispatch_webhook(subscriber, event, payload)
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
