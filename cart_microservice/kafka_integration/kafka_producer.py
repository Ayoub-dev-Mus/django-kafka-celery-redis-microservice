from confluent_kafka import Producer
from django.conf import settings
import json
import logging

logger = logging.getLogger(__name__)

def produce_message(topic, message, producer_config=None):
    if producer_config is None:
        producer_config = {
             'bootstrap.servers': 'popular-mosquito-12626-us1-kafka.upstash.io:9092',
             'sasl.mechanism': 'SCRAM-SHA-256',
             'security.protocol': 'SASL_SSL',
             'sasl.username': 'cG9wdWxhci1tb3NxdWl0by0xMjYyNiRRATTY2AVGbX4kN_EoS7nhw1Lxv5hEVtc',
             'sasl.password': 'YWE4MDlkMTctODk3MS00ZGFkLWEyOTUtNDNlMjNlMjRmYzU4',
       }

    producer = Producer(producer_config)

    try:
        serialized_message = json.dumps(message).encode('utf-8')
        producer.produce(topic, key=None, value=serialized_message)
        producer.flush()
        logger.info(f"Produced message to topic '{topic}': {message}")
    except Exception as e:
        logger.error(f"Error producing message: {e}")
    finally:

        producer.flush()
