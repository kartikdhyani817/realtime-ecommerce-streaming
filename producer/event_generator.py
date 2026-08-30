import random
import uuid
from datetime import datetime


PRODUCTS = [
    {
        "product": "Laptop",
        "category": "Electronics",
        "price": 65000
    },
    {
        "product": "Smartphone",
        "category": "Electronics",
        "price": 30000
    },
    {
        "product": "Headphones",
        "category": "Electronics",
        "price": 3000
    },
    {
        "product": "Running Shoes",
        "category": "Sports",
        "price": 4500
    },
    {
        "product": "Backpack",
        "category": "Accessories",
        "price": 2500
    },
    {
        "product": "T-Shirt",
        "category": "Fashion",
        "price": 1200
    },
    {
        "product": "Coffee Maker",
        "category": "Home",
        "price": 5500
    }
]


CITIES = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Hyderabad",
    "Pune",
    "Chennai",
    "Kolkata"
]


def generate_event():

    product = random.choice(PRODUCTS)

    quantity = random.randint(1, 3)

    unit_price = product["price"]

    total_amount = quantity * unit_price

    event = {
        "event_id": str(uuid.uuid4()),
        "order_id": f"ORD-{random.randint(10000, 99999)}",
        "customer_id": f"CUST-{random.randint(1000, 9999)}",
        "product": product["product"],
        "category": product["category"],
        "quantity": quantity,
        "unit_price": unit_price,
        "total_amount": total_amount,
        "city": random.choice(CITIES),
        "event_time": datetime.now().isoformat()
    }

    return event


if __name__ == "__main__":

    print("Generating e-commerce events...\n")

    for _ in range(10):

        event = generate_event()

        print(event)