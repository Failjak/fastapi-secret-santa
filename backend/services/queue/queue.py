import json
from typing import Union

import pika
from pika import PlainCredentials
from pydantic import BaseSettings


class QueueService:
    """ Communication with RabbitMQ service """

    def __init__(self, config: BaseSettings):
        self.config = config
        self.queue_name = self.config.queue_name

        self._connection = self._get_connection()
        self._channel = self._connection.channel()
        self._channel.queue_declare(self.queue_name)

    def get_message(self):
        """ Getting message from RabbitMQ queue """
        message = []
        if resp := self._channel.basic_get(queue=self.queue_name):
            message = self.callback(*resp)
        return message

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
            host=self.config.host,
            port=self.config.port,
            credentials=PlainCredentials(
                username=self.config.username,
                password=self.config.password
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
