from typing import Union

import pika
from pika import PlainCredentials
import json

from services.queue.config import Config


class QueueProviderService:
    """ Communication with RabbitMQ service """

    def __init__(self, config: Config):
        self.config = config
        self.queue_name = self.config.QUEUE_NAME

        self._connection = self._get_connection()
        self._channel = self._connection.channel()
        self._channel.queue_declare(self.queue_name)

    def add_message(self, message, exchange=''):
        """ Adding message to queue in RabbitMQ """

        self._channel.basic_publish(
            exchange=exchange,
            routing_key=self.queue_name,
            body=json.dumps(message).encode()
        )

    @staticmethod
    def callback(method, properties, body: Union[bytes, None]):
        """ Getting decoded body """
        return json.loads(body)

    def _get_connection(self):
        """ Getting connection to RabbitMQ """

        return pika.BlockingConnection(pika.ConnectionParameters(
            host=self.config.HOST,
            port=self.config.PORT,
            credentials=PlainCredentials(
                username=self.config.USERNAME,
                password=self.config.PASSWORD
            )
        ))

    @property
    def is_connected(self) -> bool:
        """ Returns a boolean reporting the current connection state """
        return self._connection.is_open

    def close_connection(self):
        """ Closing connection with RabbitMQ """
        self._connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()
        return True
