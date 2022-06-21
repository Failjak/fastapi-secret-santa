from aiogram import Bot, Dispatcher, executor, types
from dotenv import dotenv_values

config = dotenv_values()

bot = Bot(token=config.get('TELEGRAM_BOT_KEY'))
dp = Dispatcher(bot)


@dp.message_handler()
async def cmd_start(message: types.Message):
    print(message)
    await message.reply("You've registered. Then you will receive updates on your game. ")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
