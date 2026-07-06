"""
Configuration File
Loads subscriber information.
"""

import os
from dotenv import load_dotenv

load_dotenv()

secret1 = os.getenv("WEBHOOK_SECRET_1")
secret2 = os.getenv("WEBHOOK_SECRET_2")

if not secret1 or not secret2:
    raise ValueError(
        "Environment variables WEBHOOK_SECRET_1 and WEBHOOK_SECRET_2 are required."
    )

subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
        "secret": secret1
    },
    {
        "webhook_id": "wh02",
        "url": "https://webhook.site/",
        "secret": secret2
    }
]
