from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cart_microservice.settings')

# Create a Celery instance and configure it using the settings from Django.
celery_app = Celery('cart_microservice')

# Load task modules from all registered Django app configs.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Use JSON as the result serializer (optional, you can choose other serializers)
celery_app.conf.result_serializer = 'json'

# Set Confluent Kafka as the broker
celery_app.conf.broker_url = 'confluentkafka://cG9wdWxhci1tb3NxdWl0by0xMjYyNiRRATTY2AVGbX4kN_EoS7nhw1Lxv5hEVtc:YWE4MDlkMTctODk3MS00ZGFkLWEyOTUtNDNlMjNlMjRmYzU4@popular-mosquito-12626-us1-kafka.upstash.io:9092'


# Kafka SASL_SSL configuration
celery_app.conf.broker_transport_options = {
    'bootstrap.servers': 'popular-mosquito-12626-us1-kafka.upstash.io:9092',
    'sasl_mechanism': 'SCRAM-SHA-256',
    'security_protocol': 'SASL_SSL',
    'sasl.username': 'cG9wdWxhci1tb3NxdWl0by0xMjYyNiRRATTY2AVGbX4kN_EoS7nhw1Lxv5hEVtc',
    'sasl.password': 'YWE4MDlkMTctODk3MS00ZGFkLWEyOTUtNDNlMjNlMjRmYzU4',
    'group.id': 'test',
    'api.version.request': False,
    'auto.offset.reset': 'earliest',
}

celery_app.conf.result_backend = 'redis://localhost:6379/0'


# Auto-discover tasks in all installed apps
celery_app.autodiscover_tasks()
