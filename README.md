🚀 Webhook Notification System

⭐ Overview

This project implements a simple outbound webhook notification system in Python.

The system:

- Stores multiple webhook subscribers
- Signs webhook payloads using HMAC SHA-256
- Sends POST requests to subscribers
- Implements retry logic
- Uses environment variables to protect secret keys

---

⭐ Technologies

- Python 3.14
- Requests
- python-dotenv

---

⭐ Project Structure

```
app.py
config.py
dispatcher.py
signing.py
requirements.txt
.env.example
.gitignore
README.md
```

---

⭐ Installation

Clone the repository:

```bash
git clone https://github.com/anjaniagarwal28/Webhook-Notification-System-.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`.

Run:

```bash
py app.py
```

---

⭐ Sample Output

```json
{
    "webhook_id": "wh01",
    "event": "interview.booked",
    "status_code": 200,
    "delivery_status": "Success"
}
```

---

⭐ Security

- Secret keys are stored in `.env`.
- `.env` is excluded using `.gitignore`.
- `.env.example` is provided as a template.

---

⭐ Author

Anjani Agarwal
