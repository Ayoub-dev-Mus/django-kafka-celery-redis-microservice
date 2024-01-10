
from celery import shared_task
from kafka_integration.kafka_consumer import consume_messages

@shared_task
def run_kafka_consumer():

    topic_name = 'test'
    consume_messages(topic_name)

