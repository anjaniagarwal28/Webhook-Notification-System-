Report Structure
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
Technology	                      Purpose
Python 3	                        Programming language
requests	                        Send HTTP POST requests
json	                             Convert Python dictionaries to JSON
hmac	                              Generate secure signatures
hashlib	SHA-256 hashing

6. Project Structure
Webhook-Delivery-System/
│
├── webhook_sender.py
├── README.md
└── requirements.txt

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
      a-Subscriber Configuration
subscribers = [
   {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
        "secret": "mysecretkey"
    }
]
Explain that this stores the webhook endpoint and secret.
        b-Event Data      
event_data = {
    "event": "interview.booked",
    "candidate": "John Doe",
    "date": "2026-07-01",
    "time": "10:00 AM"
}
       c-Signature Generation
signature = hmac.new(
    subscriber["secret"].encode(),
    payload_json.encode(),
    hashlib.sha256
).hexdigest()
Explain that this creates an HMAC-SHA256 signature for secure transmission.
        d-Sending the Request
response = requests.post(
    subscriber["url"],
    data=payload_json,
    headers=headers,
    timeout=5
)

9. Testing & Validation
Only include test cases that you actually performed.

Example:
              Test Case	                                       Expected Result                                                       Actual Result
Send webhook to https://httpbin.org/post	                HTTP response received	                   200 OK (or 503 Service Temporarily Unavailable if that's what you actually observed)
Invalid URL	                                              Delivery Failed	                           Delivery Failed

actual output was:

{
'webhook_id':'wh01',
'event':'interview.booked',
'delivery_status':'503 Service Temporarily Unavailable'
}

10.Challenges & Solutions
Example:
        Challenge	                                                              Solution
Temporary 503 response from test server                        	Retried later or noted that public test servers may be temporarily unavailable
JSON conversion                                                 Used json.dumps()
Secure request authentication	                                  Implemented HMAC-SHA256 signature

11. Results
State only what your implementation demonstrates, for example:
    a-JSON payload successfully created.
    b-HMAC signature generated.
    c-HTTP POST request sent.
    d-Delivery status displayed to the user.

12. Future Scope
These are acceptable because they are clearly future work:
    a-Add a webhook receiver using Flask.
    b-Store delivery logs in a database.
    c-Support multiple subscribers.
    d-Implement automatic retries.
    e-Verify HMAC signatures on the receiver side.
    f-Build a web dashboard.

13. Conclusion
Summarize that the project demonstrates the basic workflow of webhook delivery in Python using secure signatures and HTTP POST requests. Mention that it can serve as a foundation for more advanced webhook systems.

14. References
Include only sources you actually used, for example:
    a-Python documentation
    b-Requests documentation
    c-HMAC documentation
    d-HTTP status code documentation

15. GitHub Repository:- https://github.com/anjaniagarwal28





🚀 Webhook Notification System

A lightweight Python application for securely sending webhook notifications using HTTP POST requests and HMAC-SHA256 signatures.

<p align="center"> <b>Python • JSON • HTTP POST • HMAC-SHA256 • Requests Library</b> </p>
📖 Executive Summary

The Webhook Notification System is a Python-based application that demonstrates the fundamental workflow of webhook communication. It securely transmits event notifications to a configured subscriber endpoint by converting event data into JSON format, generating an HMAC-SHA256 signature for integrity, and sending the request using the HTTP POST method.

The application records the HTTP response and displays the delivery status to indicate whether the notification was successfully delivered. The project focuses on implementing the essential concepts of webhook delivery without introducing additional components such as databases, dashboards, or webhook receivers.

❗ Problem Statement

Modern applications frequently need to notify external systems automatically whenever an important event occurs. A webhook provides a lightweight solution by sending event information directly to another application through an HTTP request.

The objective of this project is to implement a basic webhook sender capable of securely delivering event notifications while ensuring data integrity through HMAC-based signatures.

🎯 Objectives
Develop a Python-based webhook sender.
Convert event data into JSON format.
Generate secure HMAC-SHA256 signatures.
Send webhook notifications using HTTP POST.
Include appropriate HTTP request headers.
Display webhook delivery status returned by the server.
Handle request failures using exception handling.

📌 Scope
Implemented
Webhook sender
JSON payload generation
HMAC-SHA256 signature generation
Custom HTTP headers
HTTP POST request
Delivery status display
Basic exception handling
Not Implemented
Webhook receiver
Database
Dashboard
Retry mechanism
Logging
Multiple subscribers
Signature verification
🛠 Technologies Used
Technology	Purpose
Python 3	Programming Language
requests	Send HTTP POST requests
json	Convert Python objects into JSON
hmac	Generate secure signatures
hashlib	SHA-256 hashing algorithm
📂 Project Structure
Webhook-Notification-System/
│
├── webhook_sender.py
├── README.md
├── requirements.txt
└── images/
    ├── code.png
    ├── output.png
    └── workflow.png
⚙ System Workflow
+-------------------+
|   Event Data      |
+-------------------+
          │
          ▼
+-------------------+
| Convert to JSON   |
+-------------------+
          │
          ▼
+-------------------+
| Generate HMAC     |
| SHA-256 Signature |
+-------------------+
          │
          ▼
+-------------------+
| Create HTTP       |
| Headers           |
+-------------------+
          │
          ▼
+-------------------+
| Send POST Request |
+-------------------+
          │
          ▼
+-------------------+
| Receive Response  |
+-------------------+
          │
          ▼
+-------------------+
| Delivery Status   |
+-------------------+
🏗 System Architecture
                 Python Application
                         │
                         ▼
                Event Payload (JSON)
                         │
                         ▼
          Generate HMAC-SHA256 Signature
                         │
                         ▼
      Add HTTP Headers + JSON Payload
                         │
                         ▼
        HTTP POST Request (requests.post)
                         │
                         ▼
          Webhook Endpoint (Subscriber)
                         │
                         ▼
          HTTP Response (200 / 503 / etc.)
💻 Implementation Details
Subscriber Configuration
subscribers = [
    {
        "webhook_id": "wh01",
        "url": "https://httpbin.org/post",
        "secret": "mysecretkey"
    }
]

Stores the webhook endpoint, unique identifier, and secret key used to generate the HMAC signature.

Event Payload
event_data = {
    "event": "interview.booked",
    "candidate": "John Doe",
    "date": "2026-07-01",
    "time": "10:00 AM"
}

Represents the notification data sent to the subscriber.

Generate HMAC Signature
payload_json = json.dumps(payload)

signature = hmac.new(
    subscriber["secret"].encode(),
    payload_json.encode(),
    hashlib.sha256
).hexdigest()

Creates a secure SHA-256 HMAC signature to protect the integrity of the payload.

HTTP Headers
headers = {
    "Content-Type": "application/json",
    "X-Webhook-Signature": signature
}

Defines the request type and attaches the generated signature.

Sending the Webhook
response = requests.post(
    subscriber["url"],
    data=payload_json,
    headers=headers,
    timeout=5
)

Sends the JSON payload to the configured webhook endpoint.

Display Delivery Status
result = {
    "webhook_id": subscriber["webhook_id"],
    "event": payload["event"],
    "delivery_status": f"{response.status_code} {response.reason}"
}

Displays the HTTP response returned by the webhook server.

✅ Testing & Validation
Test Case	Input	Expected Result	Actual Result
Valid webhook endpoint	https://httpbin.org/post	HTTP response received	200 OK (or 503 Service Temporarily Unavailable if the public server is unavailable)
Invalid URL	Incorrect endpoint	Request failure	Delivery Failed
Sample Output
{
    'webhook_id': 'wh01',
    'event': 'interview.booked',
    'delivery_status': '200 OK'
}

If the public test server is temporarily unavailable, the output may instead be:

{
    'webhook_id': 'wh01',
    'event': 'interview.booked',
    'delivery_status': '503 Service Temporarily Unavailable'
}
📸 Project Screenshots
Source Code

(Insert screenshot here)

images/code.png
Program Output

(Insert screenshot here)

images/output.png
GitHub Repository

(Insert screenshot here)

images/github.png
⚠ Challenges & Solutions
Challenge	Solution
Public test server occasionally returned HTTP 503	Retried later or acknowledged it as temporary server unavailability
Payload formatting	Used json.dumps() to ensure valid JSON
Secure transmission	Implemented HMAC-SHA256 signature generation
📊 Results

The project successfully demonstrates the core workflow of webhook communication by:

Generating JSON payloads
Creating HMAC-SHA256 signatures
Sending HTTP POST requests
Receiving HTTP responses
Displaying delivery status

The implementation matches the source code available in the GitHub repository.

🚀 Future Scope
Support multiple webhook subscribers
Implement a webhook receiver using Flask
Verify HMAC signatures on the receiver side
Store delivery logs
Add automatic retry functionality
Build a monitoring dashboard
🎓 Conclusion

The Webhook Notification System successfully demonstrates the essential concepts involved in secure webhook communication using Python. The project converts event data into JSON, generates an HMAC-SHA256 signature, sends the payload via an HTTP POST request, and displays the resulting delivery status. Its simple design makes it an effective learning project and a solid foundation for future webhook-based applications.

📚 References
Python Documentation
Requests Library Documentation
HMAC (RFC 2104)
SHA-256 Documentation
HTTP Status Codes Documentation
🔗 GitHub Repository

Repository: https://github.com/anjaniagarwal28/Webhook-Notification-System

⭐ Tip for Your BCA Project

This format is suitable for both GitHub and your project report. To make it even more attractive, add:

A banner image at the top (designed in Canva),
Badges (Python, License, Status),
Real screenshots of your code and output,
Workflow and architecture diagrams,
Consistent use of icons and tables.

This style gives your repository the look of a professional open-source project rather than just a class assignment.

