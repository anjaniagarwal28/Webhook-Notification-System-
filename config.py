"""
config.py
Stores subscriber configuration and loads secrets from environment variables.
"""

import os

# Default demo secrets (used if .env variables are not set)
secret1 = os.getenv("WEBHOOK_SECRET_1", "demo_secret_1")
secret2 = os.getenv("WEBHOOK_SECRET_2", "demo_secret_2")

subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
        "secret": secret1
    },
    {
        "webhook_id": "wh02",
        "url": "https://httpbin.org/post",
        "secret": secret2
    }
]
