import pika
from pika import PlainCredentials

from RabbitMQ.config import config


class RabbitService:
    QUEUE_NAME = config.RABBITMQ_QUEUE_NAME

    def __init__(self):
        self.connection = self._get_connection()
        self.channel = self.connection.channel()
        self.channel.queue_declare(RabbitService.QUEUE_NAME)

    def add_message(self, message, exchange='', routing_key=QUEUE_NAME):
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=str(message).encode()
        )

    def get_message(self) -> str:
        message = self.channel.basic_get(
            queue=RabbitService.QUEUE_NAME
        )[-1]
        return message

    @staticmethod
    def _get_connection():
        return pika.BlockingConnection(pika.ConnectionParameters(
            host=config.RABBITMQ_HOST,
            port=config.RABBITMQ_PORT,
            credentials=PlainCredentials(
                username=config.RABBITMQ_USERNAME,
                password=config.RABBITMQ_PASSWORD
            )
        ))
