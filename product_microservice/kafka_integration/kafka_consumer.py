# kafka_integration/kafka_consumer.py
from confluent_kafka import Consumer, KafkaError
from django.conf import settings

def consume_messages(topic):
    bootstrap_servers = settings.KAFKA_BOOTSTRAP_SERVERS

    consumer_settings = {
             'bootstrap.servers': 'popular-mosquito-12626-us1-kafka.upstash.io:9092',
             'sasl.mechanism': 'SCRAM-SHA-256',
             'security.protocol': 'SASL_SSL',
             'sasl.username': 'cG9wdWxhci1tb3NxdWl0by0xMjYyNiRRATTY2AVGbX4kN_EoS7nhw1Lxv5hEVtc',
             'sasl.password': 'YWE4MDlkMTctODk3MS00ZGFkLWEyOTUtNDNlMjNlMjRmYzU4',
             'group.id': 'test'
}

    consumer = Consumer(consumer_settings)
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Error consuming message: {msg.error()}")
            else:
                print(f"Consumed message from topic '{topic}': {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
