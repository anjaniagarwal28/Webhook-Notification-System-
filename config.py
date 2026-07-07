import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_SECRET_1 = os.getenv("WEBHOOK_SECRET_1")
WEBHOOK_SECRET_2 = os.getenv("WEBHOOK_SECRET_2")

# Validate environment variables
if not WEBHOOK_SECRET_1 or not WEBHOOK_SECRET_2:
    raise ValueError(
        "Webhook secrets are missing. Please configure your .env file."
    )

subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
        "secret": WEBHOOK_SECRET_1
    },
    {
        "webhook_id": "wh02",
        "url": "https://httpbin.org/post",
        "secret": WEBHOOK_SECRET_2
    }
]

event = "interview.booked"

payload = {
    "candidate": "Rahul Sharma",
    "position": "Software Developer",
    "date": "03-07-2026"
}
