# Telegram-Bot

## Telegram messanger
* [Telegram - a new era of messaging](https://telegram.org/ "Telegram's official page")
    - [WebVersion] (https://web.telegram.org/)

* How do bots work?

- [Telegram bot api](https://core.telegram.org/bots/api)

* @BotFather - One bot to rule them all


- /mybots — returns a list of your bots with handy controls to edit their settings

- /mygames — does the same for your games
Edit bots

+ /setname – change your bot's name.
/setdescription — change the bot's description, a short text of up to 512 characters, describing your bot. Users will see this text at the beginning of the conversation with the bot, titled ‘What can this bot do?’.
+ /setabouttext — change the bot's about info, an even shorter text of up to 120 characters. Users will see this text on the bot's profile page. When they share your bot with someone, this text is sent together with the link.
+ /setuserpic — change the bot‘s profile pictures. It’s always nice to put a face to a name.
+ /setcommands — change the list of commands supported by your bot. Users will see these commands as suggestions when they type / in the chat with your bot. Each command has a name (must start with a slash ‘/’, alphanumeric plus underscores, no more than 32 characters, case-insensitive), parameters, and a text description. Users will see the list of commands whenever they type ‘/’ in a conversation with your bot.
+ /deletebot — delete your bot and free its username.

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

### pip

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

