Дневник разработчика Чаморцев Владимир (stud0000299683)

2024-02-17 - 2024-03-01, Спринт 1

2024-02-19

Приняли решение о реализации проекта используя следующий стек: Python 3.11 или 3.12 Framework aiogram 3.3 или 
другие аналоги. Начинаем с SQLLite далее посмотрим, по необходимости подключим Postgre sql
Возможно дальнейшее развитие в сторону Elasticsearch

2024-02-23 

Нужно изучить стек технологий для работы с TG. Читаем документацию и проходим курс на Stepik по ботам.

2024-02-26 

Бот на TG зарегистрирован.

2024-03-02 - 2024-03-16 Спринт 2


2024-03-02 

Настройка среды разработки 

2024-03-03 

Разбор проблемы с разными способами запуска проекта. VSCode запускает используя доп. файл с параметрами. 
Я пользую Pycharm, соответственно пришлось вставить первый костыль. 
Нарисовали базу данных под MVP создал скрипт позволяющий создавать базу данных. для sqlLite ничего предваритеьно делать 
не надо, а вот для postgre надо вначале создать базу данных и пользователя под которым будем соединяться к базе.

2024-03-04

Избавились от костыля, теперь все работает как надо. Для запуска в Pycharm необходимо прописывать 
доп. параметр в настройках

2024-03-09 

Изучал то что уже реализовали в проекте. Анализировал то что было в курсе на Stepic.

2024-03-10 

Переписал модель по работе с базой данных. Теперь она работает как модель данных. 
Добавил через ОРМ методы работы с базой. Добавил вывод меню из базы. Создал скрипт который позволяет провести 
первоначальное заполнение базы. Добавил Logger, пока только на главной странице. Можно еще посмотреть в сторону 
sfinks для автогенерации документации проекта. 

2024-03-11 

Развернул бота на домашнем NAS через Docker. Бот работает и отдает ответы по /url и /help 
https://t.me/NetologyStudent_bot

2024-03-12 

Небольшие правки добавил в описание данных.
Думаем над реализацией админки. 
