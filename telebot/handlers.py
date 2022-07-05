from aiogram import types

from services.bot import BotService


async def cmd_start(message: types.Message, *args, **kwargs):
    # task = handle_message.delay(message.from_user.values)
    await message.reply("You've registered. Then you will receive updates on your game. ")


async def cmd_list(message: types.Message, bot_service: BotService):
    await message.reply(bot_service.all_info().__str__())
