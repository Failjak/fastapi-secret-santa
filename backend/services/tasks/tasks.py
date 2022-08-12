import logging

from typing import List

from fastapi.logger import logger as celery_log
from celery import Celery
from celery.schedules import crontab

from database.models.player import PlayerMessage
from services.queue.config import config as queue_config
from services.tasks.config import config as celery_config
from services.queue.queue import QueueService

celery_log.setLevel(logging.DEBUG)

app = Celery(
    celery_config.name,
    broker=celery_config.broker_url,
    backend=celery_config.result_backend,
)

app.conf.beat_schedule = {
    'getting-messages-from-queue': {
        'task': 'getting_messages_from_queue',
        'schedule': crontab(minute='*/1'),
    }
}
app.conf.timezone = 'UTC'
app.conf.update(task_track_started=True)


@app.task
def send_message_to_queue_task(players: List[PlayerMessage]):
    """ Celery-task for sending messages to queue """
    celery_log.debug("Into: send_message_to_queue_task")
    with QueueService(queue_config) as provider:
        provider.add_message(players)
    celery_log.debug("Exit from: send_message_to_queue_task")
    return True


@app.task(name='getting_messages_from_queue')
def getting_messages_from_queue():
    print("Into: getting_messages_from_queue")
    with QueueService(queue_config) as consumer:
        msg = consumer.get_message()
        if not msg:
            print("NOTHING")
            celery_log.debug("NOTHING IN LOGS")
        else:
            print(f"SOMETHINGS: {msg}")
            celery_log.debug(f"SOMETHING: {msg}")
    print("Exit from: getting_messages_from_queue")
    return True
