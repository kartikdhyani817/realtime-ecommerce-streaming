import json

from kafka import KafkaConsumer

from processing.event_processor import process_event
from database.event_repository import save_event


KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "ecommerce_events"


def create_consumer():
    """Create and return a Kafka consumer."""

    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="ecommerce-consumer-group",
        value_deserializer=lambda value: json.loads(
            value.decode("utf-8")
        )
    )

    return consumer


def consume_events():
    """Read, process, and store events."""

    consumer = create_consumer()

    print("=" * 60)
    print("E-Commerce Kafka Consumer")
    print("=" * 60)
    print(f"Kafka Server : {KAFKA_SERVER}")
    print(f"Kafka Topic  : {KAFKA_TOPIC}")
    print("Database     : realtime_ecommerce")
    print()
    print("Waiting for events...")
    print()

    try:

        for message in consumer:

            raw_event = message.value

            try:

                # Step 1: Process the event
                event = process_event(raw_event)

                print(
                    f"Processed | "
                    f"Order: {event['order_id']} | "
                    f"Product: {event['product']} | "
                    f"Quantity: {event['quantity']} | "
                    f"Amount: ₹{event['total_amount']} | "
                    f"City: {event['city']}"
                )

                # Step 2: Save event to MySQL
                save_event(event)

            except ValueError as error:

                print(
                    f"Invalid event | "
                    f"Error: {error}"
                )

            except Exception as error:

                print(
                    f"Processing/Database Error | "
                    f"{error}"
                )

    except KeyboardInterrupt:

        print("\nConsumer stopped by user.")

    finally:

        consumer.close()


if __name__ == "__main__":
    consume_events()