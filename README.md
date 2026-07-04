WEBHOOK NOTIFICATION SYSTEM

A Python-based Webhook Notification System that securely sends event notifications to multiple subscribers using HTTP POST requests. The project generates HMAC-SHA256 signatures to verify payload integrity, includes timestamps for improved security, and reports delivery status based on the server response.

---

## Features

- Multiple webhook subscribers
- HMAC-SHA256 payload signing
- Timestamp included in payload
- HTTP POST webhook delivery
- Delivery status reporting
- Retry mechanism for failed requests
- Error handling
- Environment variables (.env) for secret keys

---

## Project Structure

        Webhook Notification System/
        │── app.py
        │── config.py
        │── dispatcher.py
        │── signing.py
        │── .env
        │── requirements.txt
        │── README.md

## Technologies Used

- Python 3
- requests
- python-dotenv
- json
- hmac
- hashlib

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/Webhook-Notification-System.git
```

### 2. Move into the Project Folder

```bash
cd Webhook-Notification-System
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project folder.

Example:

```env
WEBHOOK_SECRET_1=my_secret_key_1
WEBHOOK_SECRET_2=my_secret_key_2
```

---

## Configure Subscribers

Example (`config.py`):

```python
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
```

---

## Run the Project

```bash
py app.py
```

---

## Sample Output

```json
{
    "webhook_id": "wh01",
    "event": "interview.booked",
    "status_code": 200,
    "delivery_status": "Success",
    "signature": "eb2b7bcef848f60f78f2cb54f2559fe4d662e5ad2aa3d16c30a236178cd5a129"
}

{
    "webhook_id": "wh02",
    "event": "interview.booked",
    "status_code": 200,
    "delivery_status": "Success",
    "signature": "8fd53f4a3db31dce56d92a3a6aef17c8748dc9bc8c0a74db1e3b36b1d8c987a4"
}
```

---

## Project Workflow

1. Load subscriber details.
2. Create the event payload.
3. Add a timestamp.
4. Generate an HMAC-SHA256 signature.
5. Send the payload using an HTTP POST request.
6. Receive the server response.
7. Display the delivery status for each subscriber.

---

## Security Features

- HMAC-SHA256 signature generation
- Secret keys stored in `.env`
- Timestamp included in payload
- Payload integrity verification
- Basic retry mechanism for temporary failures

---

## Testing

The project was tested using the `https://httpbin.org/post` endpoint.

Successful execution returns:

- HTTP Status Code: **200**
- Delivery Status: **Success**

---

## Future Improvements

- Database integration
- Persistent logging
- Admin dashboard
- REST API
- Authentication
- Email and SMS notifications

---

## Author

**Anjani Agarwal**

Summer Training Project

---

## References

- https://docs.python.org/3/
- https://requests.readthedocs.io/
- https://pypi.org/project/python-dotenv/
- https://docs.python.org/3/library/hmac.html
- https://docs.python.org/3/library/hashlib.html

---

## License

This project is developed for educational and summer training purposes.
