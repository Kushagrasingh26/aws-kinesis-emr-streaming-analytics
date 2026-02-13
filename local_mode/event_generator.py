import json
import random
import time
from datetime import datetime

EVENT_TYPES = ["login", "purchase", "add_to_cart", "view_item", "logout"]
PRODUCTS = [f"product_{i}" for i in range(1, 51)]
USERS = [f"user_{i}" for i in range(1, 1001)]


def generate_event():
    return {
        "event_time": datetime.utcnow().isoformat(),
        "user_id": random.choice(USERS),
        "event_type": random.choice(EVENT_TYPES),
        "product_id": random.choice(PRODUCTS),
        "amount": round(random.uniform(5, 500), 2) if random.random() < 0.3 else 0.0,
    }


if __name__ == "__main__":
    while True:
        print(json.dumps(generate_event()))
        time.sleep(0.05)  # ~20 events/sec
