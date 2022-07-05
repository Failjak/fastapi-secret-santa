import random

from pydantic import BaseSettings

from services.db import DataBaseService


class BotService:
    def __init__(self, db: DataBaseService, settings: BaseSettings):
        self._db = db

    def handle_message(self, message: dict):
        result = {
            '_id': message.get('id'),
            'username': message.get('username'),
            'first_name': message.get('first_name'),
            'last_name': message.get('last_name'),
            'tmp': random.randint(1, 99)
        }
        return self._save_data(result)

    def all_info(self):
        return self._db.select(elements={}, multiple=True)

    def _save_data(self, data: dict):
        return self._db.insert(data)

