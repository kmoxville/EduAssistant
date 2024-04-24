from dataclasses import dataclass
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from sqlalchemy.orm import sessionmaker

from db_model import Menu, Answer, User
from utils import singleton
from main_menu import url_dict, session, set_main_menu


@singleton
@dataclass
class EduBot:
    bot: Bot
    token: str

    def __init__(self, config):
        self.token = config["Telegram"]["token"]

    async def start(self) -> None:
        dp = Dispatcher()

        @dp.message(CommandStart())
        async def command_start_handler(message: Message) -> None:
            # Проверяем и добавляем пользователя в базу
            user_name = message.from_user.full_name
            telegram_user_id = message.from_user.id
            existing_user = session.query(User).filter_by(telegram_user_id=telegram_user_id).first()
            if existing_user is None:
                new_user = User(telegram_user_id=telegram_user_id, user_name=user_name)
                session.add(new_user)
                session.commit()
            session.close()
            await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

        # Модель для получения Id пользователя в TG
        @dp.message(Command(commands='user_id'))
        async def start_message(message):
            await message.answer(f"Hello, your id = {message.from_user.id}!")

        # Обработка всех сообщений пользователя
        @dp.message()
        async def echo_handler(message: Message) -> None:
            try:
                # Проверяем есть ли значение в базе. Если есть то отдаем ответ
                if message.text in url_dict:
                    answer = session.query(Answer.answer).join(Menu, Menu.id == Answer.menu_id).filter(
                        Menu.url == message.text).all()
                    for row in answer:
                        await message.answer(f"{row.answer}")
                else:
                    # Если ничего не найдено, возвращаем то что пользователь ввел
                    # await message.send_copy(chat_id=message.chat.id)
                    # Если ничего не найдено, предлагаем пользователю обратиться к куратору
                    # (в данный момент ссылается на самого пользователя)
                    await message.answer(
                        f'Похоже вашего вопроса нет в базе данных, но вы можете задать его своему '
                        f'<b><a href="tg://user?id={message.from_user.id}">куратору</a></b>')

            except TypeError:
                # Если что то пошло не так выводим эту строчку
                await message.answer("Nice try!")

        bot = Bot(self.token, parse_mode=ParseMode.HTML)
        await set_main_menu(bot)
        await dp.start_polling(bot)
