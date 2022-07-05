from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from pydantic import BaseSettings

from settings import BotSettings
from services.bot import BotService
from services.mongodb import MongoService
from handlers import cmd_list, cmd_start


def main(settings: BaseSettings, bot_service: BotService) -> Dispatcher:
    bot = Bot(token=settings.telegram_bot_key)
    dispatcher = Dispatcher(bot)

    class BotServiceMiddleware(BaseMiddleware):
        async def on_pre_process_message(self, message: Message, data: dict):
            data["bot_service"] = bot_service

    dispatcher.setup_middleware(BotServiceMiddleware())

    dispatcher.register_message_handler(
        callback=cmd_list, commands=['list'],
    )
    dispatcher.register_message_handler(
        callback=cmd_start, commands=['start']
    )

    return dispatcher


if __name__ == "__main__":
    settings = BotSettings()
    db_service = MongoService()

    bot_service = BotService(db=db_service, settings=settings)

    dispatcher = main(
        settings=BotSettings(),
        bot_service=bot_service,
    )
    executor.start_polling(dispatcher, skip_updates=True)
