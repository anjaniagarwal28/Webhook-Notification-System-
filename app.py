"""
app.py
Main program.
"""

import json
import time

from dispatcher import dispatch_webhook
from config import subscribers


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

        print(
            json.dumps(
                result,
                indent=4
            )
        )


if __name__ == "__main__":
    main()