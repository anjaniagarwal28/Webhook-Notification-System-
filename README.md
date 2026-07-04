WEBHOOK NOTIFICATION SYSTEM

A Python-based Webhook Notification System that securely sends event notifications to multiple subscribers using HTTP POST requests. The project generates HMAC-SHA256 signatures to verify payload integrity, includes timestamps for improved security, and reports delivery status based on the server response.

⭐ Features

- Multiple webhook subscribers
- HMAC-SHA256 payload signing
- Timestamp for replay protection
- HTTP POST webhook delivery
- Retry mechanism
- Error handling
- Environment variables for secret keys

⭐ Technologies Used

- Python 3
- requests
- python-dotenv
- hmac
- hashlib
- json

⭐ Project Structure

```
WebhookNotificationSystem/
│── app.py
│── config.py
│── dispatcher.py
│── signing.py
│── requirements.txt
│── .env
│── README.md
```

⭐ Installation

Install the required packages:

```bash
pip install requests python-dotenv
```

⭐ Run the Project

```bash
py app.py
```

⭐ Sample Output

```json
{
    "webhook_id": "wh01",
    "event": "interview.booked",
    "status_code": 200,
    "delivery_status": "Success"
}
```

⭐ Author

Anjani Agarwal
Summer Training Project
