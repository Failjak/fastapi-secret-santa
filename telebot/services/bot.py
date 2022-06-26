import random

from .mongodb import MongoService as DBService


class BotService:
    DB = DBService

    @classmethod
    def handle_message(cls, message: dict):
        client = cls.DB()
        result = {
            '_id': message.get('id'),
            'username': message.get('username'),
            'first_name': message.get('first_name'),
            'last_name': message.get('last_name'),
            'tmp': random.randint(1, 99)
        }
        return client.insert(result)

    @classmethod
    def all_info(cls):
        client = cls.DB()
        return client.select(elements={}, multiple=True)
