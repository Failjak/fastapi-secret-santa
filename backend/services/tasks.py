from typing import List

from celery import Celery
from dotenv import dotenv_values

from database.models.player import PlayerMessage
from services.queue.provider import QueueProviderService
from services.queue.config import config as queue_config

config = dotenv_values()

app = Celery('backend')
app.conf.broker_url = config.get('CELERY_BROKER_URL', 'redis://0.0.0.0:6378')
app.conf.result_backend = config.get('CELERY_RESULT_BACKEND', 'redis://0.0.0.0:6378')


@app.task()
def send_message_to_queue_task(players: List[PlayerMessage]):
    """ Celery-task for sending messages to queue """
    with QueueProviderService(queue_config) as provider:
        provider.add_message(players)
    return True
