from aiogram import Bot, Dispatcher, executor, types
from dotenv import dotenv_values

from tasks import handle_message
from services.bot import BotService

config = dotenv_values()

bot = Bot(token=config.get('TELEGRAM_BOT_KEY'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    task = handle_message.delay(message.from_user.values)
    await message.reply("You've registered. Then you will receive updates on your game. ")


@dp.message_handler(commands='list')
async def cmd_list(message: types.Message):
    await message.reply(BotService.all_info().__str__())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
