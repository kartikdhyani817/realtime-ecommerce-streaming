from producer.kafka_producer import KAFKA_SERVER, KAFKA_TOPIC


def test_kafka_configuration():

    assert KAFKA_SERVER == "localhost:9092"
    assert KAFKA_TOPIC == "ecommerce_events"