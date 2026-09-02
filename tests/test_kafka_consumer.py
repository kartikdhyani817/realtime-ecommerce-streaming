from consumer.kafka_consumer import (
    KAFKA_SERVER,
    KAFKA_TOPIC
)


def test_consumer_configuration():

    assert KAFKA_SERVER == "localhost:9092"
    assert KAFKA_TOPIC == "ecommerce_events"