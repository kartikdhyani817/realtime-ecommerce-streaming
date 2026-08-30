from producer.event_generator import generate_event


def test_event_generation():

    event = generate_event()

    assert "event_id" in event
    assert "order_id" in event
    assert "customer_id" in event
    assert "product" in event
    assert "category" in event
    assert "quantity" in event
    assert "unit_price" in event
    assert "total_amount" in event
    assert "city" in event
    assert "event_time" in event


def test_total_amount():

    event = generate_event()

    expected_total = (
        event["quantity"] *
        event["unit_price"]
    )

    assert event["total_amount"] == expected_total