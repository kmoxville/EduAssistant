from aiogram import Bot
from aiogram.types import BotCommand
from sqlalchemy.orm import sessionmaker
from src.database.db_model import engine, Menu

# Соединяемся с БД  создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# через ORM получаем все URL из таблицы Menu
urls = session.query(Menu.url, Menu.name).all()
url_dict = {url: name for url, name in urls}


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command=url, description=name) for url, name in url_dict.items()]
    await bot.set_my_commands(main_menu_commands)
