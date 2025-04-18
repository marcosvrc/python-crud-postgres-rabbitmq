import pika
import json
import os
from dotenv import load_dotenv

load_dotenv()

class RabbitMQService:
    def __init__(self):
        self.rabbitmq_url = os.getenv("RABBITMQ_URL", "amqp://admin:admin123@localhost:5672/")
        self.queue_name = "task_events"
        self.connection = None
        self.channel = None

    def connect(self):
        if not self.connection or self.connection.is_closed:
            parameters = pika.URLParameters(self.rabbitmq_url)
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue_name, durable=True)

    def publish_event(self, event_type: str, task_data: dict):
        try:
            self.connect()
            message = {
                "event_type": event_type,
                "task_data": task_data
            }
            self.channel.basic_publish(
                exchange="",
                routing_key=self.queue_name,
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2  # make message persistent
                )
            )
        except Exception as e:
            print(f"Error publishing to RabbitMQ: {str(e)}")
        finally:
            if self.connection and not self.connection.is_closed:
                self.connection.close()

rabbitmq_service = RabbitMQService()