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
answer1 = Answer(menu=menu1, author=user1, answer='''<a href="https://netology.ru/profile">Сайт Нетологии</a> \n
Здесь ты найдешь записи прошедших занятий, а так же будешь сдавать домашку и лабораторные\n\n
<a href="https://utmn.modeus.org/">Модеус(оценки, расписание)</a>\n
Здесь ты найдешь все что касается твоего расписания в ТЮМГУ, а так же можно посмотреть свою \n
успеваемость по предметам\n\n
<a href="https://lms.utmn.ru/my/">LMS - онлайн лекции</a>\n
Данный ресурс позволит тебе просматривать часть лекций ТЮМГУ, которые были предварительно записаны\n
а так же тут можно сдавать тесты по дисциплинам.\n\n
<a href="https://mail.utmn.ru/">корпоративная почта студента</a>\n
Не забывай читать почту, там бывает довольно важная инфомация касаемая учебного процесса.\n\n
''')

answer2 = Answer(menu=menu2, author=user1, answer='''Список доступных команд:\n\n
/start - начать все сначала\n
/url - ссылки\n
/user_id - получить свой идентификатор в ТГ\n
''')

# Добавление объектов в сессию и сохранение изменений
session.add_all([user1, menu1, menu2, answer1, answer2])
session.commit()

# Закрытие сессии
session.close()
