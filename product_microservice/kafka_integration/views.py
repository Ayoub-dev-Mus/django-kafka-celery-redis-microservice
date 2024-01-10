# kafka_integration/views.py
from django.http import HttpResponse
from kafka_integration.tasks import run_kafka_consumer
from kafka_integration.kafka_producer import produce_message
from kafka_integration.kafka_consumer import consume_messages

def send_kafka_message(request , message):
    print("Entering send_kafka_message view")
    produce_message('test',message)
    return HttpResponse("Kafka message sent successfully.")

def start_kafka_consumer(request):
    try:
        print("Entering start_kafka_consumer view")
        consumed = consume_messages('test')
        print(consumed)
        run_kafka_consumer.delay()
        return HttpResponse("Kafka consumer task started successfully.")
    except Exception as e:
        print(f"Error starting Kafka consumer task: {str(e)}")
        return HttpResponse(f"Error starting Kafka consumer task: {str(e)}")
