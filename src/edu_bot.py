import asyncio
from typing import Any

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from dataclasses import dataclass
from utils import singleton

@singleton
@dataclass
class EduBot():
    bot: Bot
    token: str

    def __init__(self, config):
        self.token = config["Telegram"]["token"]

    async def start(self) -> None:
        dp = Dispatcher()

        @dp.message(CommandStart())
        async def command_start_handler(message: Message) -> None:
            await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


        @dp.message()
        async def echo_handler(message: types.Message) -> None:
            try:
                # Send a copy of the received message
                await message.send_copy(chat_id=message.chat.id)
            except TypeError:
                # But not all the types is supported to be copied so need to handle it
                await message.answer("Nice try!")
                

        bot = Bot(self.token, parse_mode=ParseMode.HTML)
        await dp.start_polling(bot)