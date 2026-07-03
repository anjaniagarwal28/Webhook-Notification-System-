"""
config.py
Loads environment variables and stores subscriber details.
"""

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
        "secret": os.getenv("WEBHOOK_SECRET_1")
    },
    {
        "webhook_id": "wh02",
        "url": "https://httpbin.org/post",
        "secret": os.getenv("WEBHOOK_SECRET_2")
    }
]
