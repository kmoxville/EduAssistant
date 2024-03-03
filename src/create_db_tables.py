from sqlalchemy import create_engine, Column, Integer, MetaData, Table, Text, ForeignKey, VARCHAR, BOOLEAN
from config_loader import load_config

# Загружаем данные из конфига


config = load_config("config.yaml")

# Присваиваем переменные для дальнейшего более простого использования
bot_token = config['Telegram']['token']
superadmin = config['Admins']
db_name = config['Database']['database_name']
db_user = config['Database']['username']
pwd = config['Database']['password']
db_host = config['Database']['host']

# Соединяемся с базой данных Postgresql
# engine = create_engine(f'postgresql://{db_user}:{pwd}@{db_host}:5432/{db_name}')
# Для соединения с sqlLite
engine = create_engine('sqlite:///sqlite3.db')

engine.connect()

# Далее создаем таблицы в базе данных. Если таблицы уже есть то ничего не создается.
# Да и если используем Postgresql то вначале надо создать базу.

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer(), primary_key=True),
              Column('telegram_user_id', Integer(), nullable=False),
              Column('user_name', VARCHAR(30), nullable=False),
              Column('is_admin', BOOLEAN, default=False),
              #    Column('role_id', Integer(), ForeignKey('roles.id')),
              )

menu = Table('menu', metadata,
             Column('id', Integer(), primary_key=True),
             Column('sub_id', Integer, ForeignKey('menu.id'), nullable=True),
             Column('name', VARCHAR(20), nullable=False),
             Column('url', VARCHAR(10), nullable=False), )

answers = Table('answers', metadata,
                Column('id', Integer(), primary_key=True),
                Column('menu_id', Integer(), ForeignKey('menu.id')),
                Column('authtor_id', Integer(), ForeignKey('users.id')),
                Column('answer', Text, nullable=False), )

metadata.create_all(engine)
