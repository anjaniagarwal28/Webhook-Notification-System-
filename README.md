WEBHOOK NOTIFICATION SYSTEM

The Webhook Notification System is implemented using Python and demonstrates the basic workflow of a webhook notification. The application stores subscriber information, creates an event payload, generates a secure HMAC-SHA256 signature, simulates webhook delivery, and displays the delivery status in JSON format.


1. Importing Required Libraries

        import json
        import hmac
        import hashlib

The program begins by importing three built-in Python libraries:

- json: Converts Python dictionaries into JSON format, which is the standard format for exchanging data between applications.

- hmac: Generates a Hash-based Message Authentication Code (HMAC) to verify the authenticity and integrity of the webhook payload.

- hashlib: Provides cryptographic hash functions such as SHA-256, which is used to generate a secure signature.

- These libraries are sufficient to implement a basic webhook simulation without relying on external packages.


2. Storing Webhook Subscriber Information

        subscribers = [
            {
                  "webhook_id": "wh01",
                  "url": "https://example.com/webhook",
                  "secret": "my_secret_key"
             }
        ]

The subscribers list stores information about webhook subscribers. Each subscriber is represented as a dictionary containing:

- webhook_id – A unique identifier for the subscriber.

- url – The webhook endpoint where notifications would be sent.

- secret – A private key used to generate an HMAC signature for secure communication.

Although only one subscriber is included in this implementation, the list structure allows additional subscribers to be added easily.


3. Defining the Event

        event = "interview.booked"

The event variable represents the webhook event that will be delivered to subscribers.

In this project, the event is:

        interview.booked

This indicates that an interview has been successfully scheduled.


4. Creating the Payload

        payload = {
            "candidate": "Rahul Sharma",
            "position": "Software Developer",
            "date": "03-07-2026"
        }

The payload contains the information associated with the event.

It includes:

        Candidate Name
        Job Position
        Interview Date

Before transmission, the payload is converted into JSON format.


5. Generating the HMAC Signature
def generate_signature(secret, payload):

           message = json.dumps(payload).encode()
           signature = hmac.new(
                   secret.encode(),
                    message,
                    hashlib.sha256
            ).hexdigest()
            return signature


This function generates a secure HMAC-SHA256 signature for the payload.

Working Process
- Converts the payload into a JSON string.
- Encodes the JSON data into bytes.
- Uses the subscriber's secret key.
- Applies the SHA-256 hashing algorithm.
- Generates a hexadecimal signature.

The generated signature ensures:

- Data integrity
- Message authenticity
- Protection against payload tampering

6. Simulating Webhook Delivery

        def dispatch_webhook(subscriber, event, payload):

This function simulates sending the webhook notification to a subscriber.

Inside the function:

        signature = generate_signature(subscriber["secret"], payload)

The program first generates the HMAC signature using the subscriber's secret key.
Simulated Delivery Status

        delivery_status = "200 OK"

Instead of making an actual HTTP POST request, the program simulates a successful webhook response.

The HTTP status 200 OK indicates that the webhook was delivered successfully.

7. Preparing the Output

        result = {
            "webhook_id": subscriber["webhook_id"],
            "event": event,
            "delivery_status": delivery_status
           }

A dictionary is created to store the final webhook delivery result.

It contains:

- Webhook ID
- Event Name
- Delivery Status

This output represents the final response of the webhook notification system.

8. Returning the Result
- return result

The function returns the generated result dictionary to the main program.

9. Sending Notifications

        for subscriber in subscribers:
            output = dispatch_webhook(subscriber, event, payload)
            print(json.dumps(output, indent=4))

The program iterates through the list of subscribers.

For each subscriber:
- Generates the HMAC signature.
- Simulates webhook delivery.
- Creates the response.
- Displays the output in a formatted JSON structure.

The indent=4 parameter improves readability by printing the JSON in a well-structured format.

Program Workflow
        
         Start
           │
           ▼
        Import Required Libraries
           │
           ▼
        Store Subscriber Information
           │
           ▼
        Create Event Payload
           │
           ▼
        Generate HMAC-SHA256 Signature
           │
           ▼
        Simulate Webhook Delivery
           │
           ▼
        Create Result Dictionary
           │
           ▼
        Display JSON Output
           │
           ▼
        End
Output
        
        {
            "webhook_id": "wh01",
            "event": "interview.booked",
            "delivery_status": "200 OK"
        }
