1. Executive Summary

Describe that the project implements a basic webhook sender in Python. It securely sends JSON event data to a subscriber URL using HTTP POST and includes an HMAC-SHA256 signature in the request headers. The program reports whether the delivery was successful based on the HTTP response.


2. Problem Statement

Many applications need to notify external systems automatically when an event occurs. This project demonstrates how to send such notifications securely using webhooks.


3. Objectives

Implement webhook delivery using Python.

Send event data as JSON.

Generate an HMAC-SHA256 signature.

Include custom HTTP headers.

Display the delivery status.


4. Scope

This project is limited to sending a webhook to a single subscriber. It does not include webhook receiving, authentication beyond HMAC generation, databases, retry mechanisms, or graphical interfaces.


5. Technologies Used

      Technology	                        Purpose

      Python 3	                   Programming language

      requests	                   Send HTTP POST requests

      json	                         Convert Python dictionaries to JSON

      hmac	                         Generate secure signatures

      hashlib	                    SHA-256 hashing


6. Project Structure

Webhook-Delivery-System/
│
├── webhook_sender.py
├── README.md
└── requirements.txt

Only include files that actually exist in your GitHub repository.

7. System Workflow
Event Data
      │
      ▼
Convert to JSON
      │
      ▼
Generate HMAC Signature
      │
      ▼
Create HTTP Headers
      │
      ▼
Send POST Request
      │
      ▼
Receive HTTP Response
      │
      ▼
Display Delivery Status
8. Implementation Details

Include short snippets like:

Subscriber Configuration
subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
        "secret": "mysecretkey"
    }
]

Explain that this stores the webhook endpoint and secret.

Event Data
event_data = {
    "event": "interview.booked",
    "candidate": "John Doe",
    "date": "2026-07-01",
    "time": "10:00 AM"
}
Signature Generation
signature = hmac.new(
    subscriber["secret"].encode(),
    payload_json.encode(),
    hashlib.sha256
).hexdigest()

Explain that this creates an HMAC-SHA256 signature for secure transmission.

Sending the Request
response = requests.post(
    subscriber["url"],
    data=payload_json,
    headers=headers,
    timeout=5
)
9. Testing & Validation

Only include test cases that you actually performed.

Example:

Test Case	Expected Result	Actual Result
Send webhook to https://httpbin.org/post	HTTP response received	200 OK (or 503 Service Temporarily Unavailable if that's what you actually observed)
Invalid URL	Delivery Failed	Delivery Failed

If your actual output was:

{
'webhook_id':'wh01',
'event':'interview.booked',
'delivery_status':'503 Service Temporarily Unavailable'
}

then include that exact output. Do not replace it with 200 OK unless you actually obtained that result.

Include screenshots of:

VS Code
Terminal output
GitHub repository
10. Challenges & Solutions

Example:

Challenge	Solution
Temporary 503 response from test server	Retried later or noted that public test servers may be temporarily unavailable
JSON conversion	Used json.dumps()
Secure request authentication	Implemented HMAC-SHA256 signature
11. Results

State only what your implementation demonstrates, for example:

JSON payload successfully created.
HMAC signature generated.
HTTP POST request sent.
Delivery status displayed to the user.
12. Future Scope

These are acceptable because they are clearly future work:

Add a webhook receiver using Flask.
Store delivery logs in a database.
Support multiple subscribers.
Implement automatic retries.
Verify HMAC signatures on the receiver side.
Build a web dashboard.
13. Conclusion

Summarize that the project demonstrates the basic workflow of webhook delivery in Python using secure signatures and HTTP POST requests. Mention that it can serve as a foundation for more advanced webhook systems.

14. References

Include only sources you actually used, for example:

Python documentation
Requests documentation
HMAC documentation
HTTP status code documentation
15. GitHub Repository
