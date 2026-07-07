import json
from config import subscribers, event, payload
from dispatcher import dispatch_webhook


def main():
    print("=" * 60)
    print("WEBHOOK NOTIFICATION SYSTEM")
    print("=" * 60)

    for subscriber in subscribers:
        result = dispatch_webhook(
            subscriber,
            event,
            payload
        )

        print(json.dumps(result, indent=4))
        print()


if __name__ == "__main__":
    main()
