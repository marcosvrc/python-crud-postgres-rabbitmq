import pika
import json
import os
from dotenv import load_dotenv

load_dotenv()

def callback(ch, method, properties, body):
    try:
        message = json.loads(body)
        event_type = message.get("event_type")
        task_data = message.get("task_data")
        
        print(f"Received {event_type} event:")
        print(f"Task data: {json.dumps(task_data, indent=2)}")
        
        # Aqui você pode adicionar lógica adicional para processar os eventos
        # Por exemplo, enviar notificações, atualizar cache, etc.
        
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Error processing message: {str(e)}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

def start_consuming():
    rabbitmq_url = os.getenv("RABBITMQ_URL", "amqp://admin:admin123@localhost:5672/")
    queue_name = "task_events"
    
    try:
        parameters = pika.URLParameters(rabbitmq_url)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        
        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, on_message_callback=callback)
        
        print("Started consuming messages from RabbitMQ...")
        channel.start_consuming()
    except Exception as e:
        print(f"Error connecting to RabbitMQ: {str(e)}")

if __name__ == "__main__":
    start_consuming()