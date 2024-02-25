# EduAssistant
#### Description
todo

#### Run and debug
1.  Регистрируем бота через Bot.Father, получаем токен
2. Для тех, кто пользуется vcs, создаем launch.json с примерно таким содержанием:

```
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python Debugger",
                "type": "debugpy",
                "request": "launch",
                "program": "src/edu_assistant.py",
                "cwd": "${workspaceFolder}",
                "args": [
                    "--token", "YOUR_TOKEN",
                ],
                "console": "integratedTerminal"
            }
        ]
    }
```

3. На место YOUR_TOKEN подставляем свой токен
4. Запускаем
