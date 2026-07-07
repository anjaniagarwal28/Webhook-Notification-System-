"""
config.py
Loads environment variables and stores subscriber details.
"""

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

secret1 = os.getenv("WEBHOOK_SECRET_1")
secret2 = os.getenv("WEBHOOK_SECRET_2")

# Validate secrets
if not secret1 or not secret2:
    raise ValueError(
        "Environment variables WEBHOOK_SECRET_1 and WEBHOOK_SECRET_2 must be set."
    )

subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
        "secret": secret1,
    },
    {
        "webhook_id": "wh02",
        "url": "https://httpbin.org/post",
        "secret": secret2,
    },
]
