import json
import time

from kafka import KafkaProducer

from producer.event_generator import generate_event


KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "ecommerce_events"


def create_producer():
    """Create and return a Kafka producer."""

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda value: json.dumps(value).encode("utf-8")
    )

    return producer


def send_events(number_of_events=10, delay=1):
    """Generate and send e-commerce events to Kafka."""

    producer = create_producer()

    print("=" * 60)
    print("E-Commerce Kafka Producer")
    print("=" * 60)
    print(f"Kafka Server : {KAFKA_SERVER}")
    print(f"Kafka Topic  : {KAFKA_TOPIC}")
    print(f"Events       : {number_of_events}")
    print()

    try:
        for i in range(number_of_events):

            event = generate_event()

            producer.send(
                KAFKA_TOPIC,
                value=event
            )

            print(
                f"Event {i + 1}/{number_of_events} sent | "
                f"Order: {event['order_id']} | "
                f"Product: {event['product']} | "
                f"Amount: ₹{event['total_amount']}"
            )

            time.sleep(delay)

        producer.flush()

        print()
        print("All events successfully sent to Kafka.")

    except Exception as error:

        print()
        print("Kafka Producer Error:")
        print(error)

    finally:
        producer.close()


if __name__ == "__main__":
    send_events(
        number_of_events=10,
        delay=1
    )