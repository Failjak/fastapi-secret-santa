from dotenv import dotenv_values

from celery import Celery

from services.bot import BotService

config = dotenv_values()

app = Celery('telebot', broker=config.get('CELERY_BROKER_URL'), backend=config.get('CELERY_RESULT_BACKEND'))


@app.task
def handle_message(message: dict):
    BotService.handle_message(message)

