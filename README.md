# EduAssistant
#### Description
todo
Можно прикрутить Sphinks для автоматической генерации документации.
 
#### Run and debug
1.  Регистрируем бота через BotFather, получаем токен
2. Для тех, кто пользуется vcs, создаем launch.json с примерно таким содержанием:

```
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python Debugger",
                "type": "debugpy",
                "request": "launch",
                "program": "src/main.py",
                "cwd": "${workspaceFolder}",
                "args": [
                    "--config", "YOUR_CONFIG_FILE",
                ],
                "console": "integratedTerminal"
            }
        ]
    }
```
2.1 Если используете PyCharm то в настройках необходимо в script parametr прописать  --config "config/config.yaml"
3. На место YOUR_CONFIG_FILE подставляем свой путь к файлу конфигурации, шаблон в папке config скопировать можете
4. Запускаем main.py и app.py 
Main.py - запускает бота 
app.py - запускает web admin

Сам проект создан командой ПИР2 
Работает на Python 3.11
Библиотеки для использования смотри в файле requirements.txt