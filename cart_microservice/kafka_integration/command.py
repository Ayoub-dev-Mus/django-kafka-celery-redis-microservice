# kafka_integration/management/commands/consume_kafka_messages.py
from django.core.management.base import BaseCommand
from kafka_integration.kafka_consumer import consume_messages

class Command(BaseCommand):
    help = 'Consume Kafka messages related to products'

    def handle(self, *args, **options):
        topic_name = 'test'
        consume_messages(topic_name)
