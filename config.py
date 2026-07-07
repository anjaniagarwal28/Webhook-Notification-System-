"""
<<<<<<< HEAD
config.py
Loads environment variables and stores subscriber details.
=======
Configuration File
Loads subscriber information.
>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
"""

import os
from dotenv import load_dotenv

<<<<<<< HEAD
# Load variables from .env
load_dotenv()

=======
load_dotenv()

secret1 = os.getenv("WEBHOOK_SECRET_1")
secret2 = os.getenv("WEBHOOK_SECRET_2")

if not secret1 or not secret2:
    raise ValueError(
        "Environment variables WEBHOOK_SECRET_1 and WEBHOOK_SECRET_2 are required."
    )

>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
<<<<<<< HEAD
        "secret": os.getenv("WEBHOOK_SECRET_1")
    },
    {
        "webhook_id": "wh02",
        "url": "https://httpbin.org/post",
        "secret": os.getenv("WEBHOOK_SECRET_2")
    }
]
=======
        "secret": secret1
    },
    {
        "webhook_id": "wh02",
        "url": "https://webhook.site/",
        "secret": secret2
    }
]
>>>>>>> be47dc0c1c1a52988733a6c99359a43807e7b218
