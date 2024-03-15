from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_model import User, Menu, Answer

# Создание соединения с базой данных
engine = create_engine('sqlite:///sqlite3.db')

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Создание пользователей
user1 = User(telegram_user_id=420443281, user_name='Vladimir', is_admin=True)

# Создание пунктов меню
menu1 = Menu(name='url', url='/url')
menu2 = Menu(name='help', url='/help')

# Создание ответов
answer1 = Answer(menu=menu1, author=user1, answer='''<a href="https://netology.ru/profile">Сайт Нетологии</a>
Здесь ты найдешь записи прошедших занятий, а так же будешь сдавать домашку и лабораторные\n
<a href="https://utmn.modeus.org/">Модеус(оценки, расписание)</a>
Здесь ты найдешь все что касается твоего расписания в ТЮМГУ, а так же можно посмотреть свою
успеваемость по предметам\n
<a href="https://lms.utmn.ru/my/">LMS - онлайн лекции</a>
Данный ресурс позволит тебе просматривать часть лекций ТЮМГУ, которые были предварительно записаны
а так же тут можно сдавать тесты по дисциплинам.\n
<a href="https://mail.utmn.ru/">корпоративная почта студента</a>
Не забывай читать почту, там бывает довольно важная инфомация касаемая учебного процесса.\n
''')

answer2 = Answer(menu=menu2, author=user1, answer='''Список доступных команд:\n
/start - начать все сначала
/url - ссылки
/user_id - получить свой идентификатор в ТГ
''')

# Добавление объектов в сессию и сохранение изменений
session.add_all([user1, menu1, menu2, answer1, answer2])
session.commit()

# Закрытие сессии
session.close()
