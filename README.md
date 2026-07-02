🚀REPORT FILE


📑Executive Summary

Describe that the project implements a basic webhook sender in Python. It securely sends JSON event data to a subscriber URL using HTTP POST and includes an HMAC-SHA256 signature in the request headers. The program reports whether the delivery was successful based on the HTTP response.


❗Problem Statement

Many applications need to notify external systems automatically when an event occurs. This project demonstrates how to send such notifications securely using webhooks.


🎯 Objectives

         🔸Implement webhook delivery using Python.

         🔸Send event data as JSON.

         🔸Generate an HMAC-SHA256 signature.

         🔸Include custom HTTP headers.

         🔸Display the delivery status.


📌 Scope

This project is limited to sending a webhook to a single subscriber. It does not include webhook receiving, authentication beyond HMAC generation, databases, retry mechanisms, or graphical interfaces.


🛠 Technologies Used

         Technology                          Purpose

         Python 3                            Programming language

         requests                            Send HTTP POST requests

         json                                Convert Python dictionaries to JSON
   
         hmac                                Generate secure signatures
   
         hashlib                             SHA-256 hashing


📂 Project Structure

         Webhook-Delivery-System/
         
         │

         ├── webhook_sender.py

         ├── README.md

         └── requirements.txt

Only include files that actually exist in our GitHub repository.


⚙️ System Workflow

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


💻 Implementation Details

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


🧪 Testing & Validation

Only include test cases that you actually performed.

Example:

      Test Case	                                        Expected Result	            Actual Result

      Send webhook to https://httpbi n.org/post	          HTTP response received	      200 OK (or 503 Service Temporarily Unavailable)

      Invalid URL                                         Delivery Failed	            Delivery Failed

 Our actual output was:

      {

         'webhook_id':'wh01',

         'event':'interview.booked',

         'delivery_status':'503 Service Temporarily Unavailable'

      }


⚠️ Challenges & Solutions

Example:

      Challenge	                                        Solution
      
      Temporary 503 response from test server	         Retried later or noted that public test servers may be temporarily unavailable
      
      JSON conversion	                                 Used json.dumps()
      
      Secure request authentication	                     Implemented HMAC-SHA256 signature


📊 Results

State only what your implementation demonstrates, for example:

JSON payload successfully created.

HMAC signature generated.

HTTP POST request sent.

Delivery status displayed to the user.


🔮 Future Scope

These are acceptable because they are clearly future work:

Add a webhook receiver using Flask.

Store delivery logs in a database.

Support multiple subscribers.

Implement automatic retries.

Verify HMAC signatures on the receiver side.

Build a web dashboard.


🎓 Conclusion

Summarize that the project demonstrates the basic workflow of webhook delivery in Python using secure signatures and HTTP POST requests. Mention that it can serve as a foundation for more advanced webhook systems.


📚 References

Include only sources you actually used, for example:

Python documentation

Requests documentation

HMAC documentation

HTTP status code documentation


🔗 GitHub Repository

         Github: https://github.com/anjaniagarwal28
