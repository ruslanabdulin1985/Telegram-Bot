# Telegram-Bot

## Telegram messanger
* [Telegram - a new era of messaging](https://telegram.org/ "Telegram's official page")
    - [WebVersion] (https://web.telegram.org/)

* How do bots work?
- [Telegram bot introduction](https://core.telegram.org/bots)
- [Telegram bot api](https://core.telegram.org/bots/api)

* @BotFather - One bot to rule them all

## HTTP requests

*All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: https://api.telegram.org/bot<token>/METHOD_NAME. Like this for example
    - get me : https://api.telegram.org/bot957417052:AAHLnkugOejglnzeY5141FahYxxYcuhOjyE/getMe
    - get updates : https://api.telegram.org/bot957417052:AAHLnkugOejglnzeY5141FahYxxYcuhOjyE/getUpdates
    - send message: https://api.telegram.org/bot957417052:AAHLnkugOejglnzeY5141FahYxxYcuhOjyE/sendMessage?chat_id=863183318&text=test


https://api.telegram.org/bot<token>/METHOD_NAME

## JSON editor

[JSON Editor Online] (https://jsoneditoronline.org)

## Python

[Python](https://www.python.org/)

[PyCharm](https://www.jetbrains.com/pycharm/)

[pypi project](https://pypi.org/project/pip/)

### Install/Update pip

Linux : sudo apt-get install python3-pip

Update pip install -U pip

﻿Windows : python.exe -m pip install --upgrade pip

### Telebot

[pyTelegramBotApi](https://github.com/eternnoir/pyTelegramBotAPI)

﻿python.exe -m pip install pyTelegramBotApi

python3 -m pip install pyTelegramBotApi


## Echo
def Echo(message):
    Bot.send_message(message.from_user.id, message.text)

## Buttons
    if message.text == "button":
        Bot.send_message(message.from_user.id, "Button Accepted!")

## Interactions
    def RandomTyping(message):
        Bot.send_chat_action(message.from_user.id, "typing")
        time.sleep(random.randint(3, 6))

