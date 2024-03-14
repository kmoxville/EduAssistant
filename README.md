# EduAssistant
#### Description
todo

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

3. На место YOUR_CONFIG_FILE подставляем свой путь к файлу конфигурации, шаблон в папке config скопировать можете
4. Запускаем
