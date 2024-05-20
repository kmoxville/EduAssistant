from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey, String, Boolean, DateTime
from src.config.config_loader import load_config
from sqlalchemy.orm import declarative_base
from datetime import datetime
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '../..'))

# Загружаем данные из конфига


config = load_config("../config/config.yaml")

# Присваиваем переменные для дальнейшего более простого использования
bot_token = config['Telegram']['token']
superadmin = config['Admins']['telegram_user_id']
superadmin_name = config['Admins']['user_name']
db_name = config['Database']['database_name']
db_user = config['Database']['username']
pwd = config['Database']['password']
db_host = config['Database']['host']

# Соединяемся с базой данных Postgresql
# engine = create_engine(f'postgresql://{db_user}:{pwd}@{db_host}:5432/{db_name}')
# Для соединения с sqlLite

db = os.path.join('c:/Users/chamorcev/PycharmProjects/EduAssistant/src/database/', 'sqlite3.db')

engine = create_engine(f'sqlite:///{db}')


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_user_id = Column(Integer, nullable=False)
    user_name = Column(String(30), nullable=False)
    is_admin = Column(Boolean, default=False)
    active = Column(Boolean, default=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now)


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    sub_id = Column(Integer, ForeignKey('menu.id'), nullable=True)
    name = Column(String(20), nullable=False)
    url = Column(String(10), nullable=False)
    active = Column(Boolean, default=False)
    answer = Column(Text, default=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now)


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    score = Column(Text, nullable=False)
    keywords = Column(Text, nullable=False)


Base.metadata.create_all(engine)
