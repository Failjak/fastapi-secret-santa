from dotenv import dotenv_values

from celery import Celery

from services.bot import BotService

config = dotenv_values()

app = Celery('telebot')
app.conf.broker_url = config.get('CELERY_BROKER_URL', 'redis://0.0.0.0:6378')
app.conf.result_backend = config.get('CELERY_RESULT_BACKEND', 'redis://0.0.0.0:6378')


@app.task
def handle_message(message: dict):
    BotService.handle_message(message)

