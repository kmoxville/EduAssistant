from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_model import User, Menu, Answer, superadmin, superadmin_name

# Создание соединения с базой данных
engine = create_engine('sqlite:///sqlite3.db')

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Создание пользователей
user1 = User(telegram_user_id=superadmin, user_name=superadmin_name, is_admin=True)

# Создание пунктов меню
menu1 = Menu(name='url', url='/url')
menu2 = Menu(name='help', url='/help')
menu3 = Menu(name='pay', url='/pay')

# Создание ответов
answer1 = Answer(menu=menu1, author=user1, answer='''https://netology.ru/profile Сайт Нетологии \n
Здесь ты найдешь записи прошедших занятий, а так же будешь сдавать домашку и лабораторные\n
https://utmn.modeus.org/ Модеус(оценки, расписание \n
Здесь ты найдешь все что касается твоего расписания в ТЮМГУ, а так же можно посмотреть свою
успеваемость по предметам\n
https://lms.utmn.ru/my/ LMS - онлайн лекции\n
Данный ресурс позволит тебе просматривать часть лекций ТЮМГУ, которые были предварительно записаны
а так же тут можно сдавать тесты по дисциплинам.\n
https://mail.utmn.ru/ корпоративная почта студента \n
Не забывай читать почту, там бывает довольно важная инфомация касаемая учебного процесса.\n
''')

answer2 = Answer(menu=menu2, author=user1, answer='''Список доступных команд:\n
/start - начать все сначала
/url - ссылки
/user_id - получить свой идентификатор в ТГ
/pay
''')

answer3 = Answer(menu=menu3, author=user1, answer='''https://www.utmn.ru/pay/\n
Совершить оплату вы можете через платёжный сервис ТюмГУ. Согласно договору оплату необходимо вносить два раза в год 
до 15 декабря и до 15 июля.
''')

# Добавление объектов в сессию и сохранение изменений
session.add_all([user1, menu1, menu2, menu3, answer1, answer2, answer3])
session.commit()

# Закрытие сессии
session.close()
