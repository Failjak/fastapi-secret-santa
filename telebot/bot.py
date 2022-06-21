import logging
from aiogram import Bot, Dispatcher, executor, types

# from core.config import settings

bot = Bot(token='5574037701:AAHVn2itsfgI8U7IfJ1woGWdg0wEy2SnWxc')
dp = Dispatcher(bot)


logging.basicConfig(level=logging.INFO)


@dp.message_handler()
async def cmd_start(message: types.Message):
    await message.reply("You've registered. Then you will receive updates on your game. ")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
