from datetime import datetime


REQUIRED_FIELDS = [
    "event_id",
    "order_id",
    "customer_id",
    "product",
    "category",
    "quantity",
    "unit_price",
    "total_amount",
    "city",
    "event_time",
]


def validate_event(event):
    """Validate that an event contains all required fields."""

    missing_fields = [
        field for field in REQUIRED_FIELDS
        if field not in event
    ]

    if missing_fields:
        raise ValueError(
            f"Missing required fields: {missing_fields}"
        )

    if event["quantity"] <= 0:
        raise ValueError("Quantity must be greater than 0")

    if event["unit_price"] < 0:
        raise ValueError("Unit price cannot be negative")

    if event["total_amount"] < 0:
        raise ValueError("Total amount cannot be negative")

    return True


def process_event(event):
    """Validate and transform a raw e-commerce event."""

    validate_event(event)

    processed_event = event.copy()

    # Normalize text fields
    processed_event["product"] = event["product"].strip().title()
    processed_event["category"] = event["category"].strip().title()
    processed_event["city"] = event["city"].strip().title()

    # Convert numeric values to consistent types
    processed_event["quantity"] = int(event["quantity"])
    processed_event["unit_price"] = float(event["unit_price"])
    processed_event["total_amount"] = float(event["total_amount"])

    # Validate event timestamp
    datetime.fromisoformat(event["event_time"])

    # Add processing timestamp
    processed_event["processed_at"] = datetime.now().isoformat()

    return processed_event


if __name__ == "__main__":
    sample_event = {
        "event_id": "test-event",
        "order_id": "ORD-10001",
        "customer_id": "CUST-1001",
        "product": " laptop ",
        "category": " electronics ",
        "quantity": 2,
        "unit_price": 50000,
        "total_amount": 100000,
        "city": " delhi ",
        "event_time": datetime.now().isoformat(),
    }

    result = process_event(sample_event)

    print("Processed Event:")
    print(result)