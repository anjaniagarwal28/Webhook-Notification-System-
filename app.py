"""
<<<<<<< HEAD
app.py
Main program.
"""

import json
import time

from dispatcher import dispatch_webhook
from config import subscribers


def main():

=======
Main entry point for Webhook Notification System
"""

import json
from config import subscribers
from dispatcher import dispatch_webhook


def main():
>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
    event = "interview.booked"

    payload = {
        "candidate": "Rahul Sharma",
        "position": "Software Developer",
<<<<<<< HEAD
        "date": "03-07-2026",
        "timestamp": int(time.time())
    }

    if not subscribers:

        print("No subscribers found.")
        return

=======
        "date": "03-07-2026"
    }

>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
    print("=" * 60)
    print("WEBHOOK NOTIFICATION SYSTEM")
    print("=" * 60)

<<<<<<< HEAD
    for subscriber in subscribers:

        result = dispatch_webhook(
            subscriber,
            event,
            payload
        )

        print(
            json.dumps(
                result,
                indent=4
            )
        )


if __name__ == "__main__":
    main()
=======
    if not subscribers:
        print("No subscribers found.")
        return

    for subscriber in subscribers:
        result = dispatch_webhook(subscriber, event, payload)
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
