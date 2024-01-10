# urls.py
from django.urls import path
from .views import start_kafka_consumer , send_kafka_message

urlpatterns = [
    path('start_kafka_consumer/', start_kafka_consumer, name='start_kafka_consumer'),
    path('send_kafka_message/', send_kafka_message, name='send_kafka_message'),
]
