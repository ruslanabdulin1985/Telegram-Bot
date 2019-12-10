import telebot
import time
import random

Bot = telebot.TeleBot("957417052:AAHLnkugOejglnzeY5141FahYxxYcuhOjyE")


@Bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    random_typing(message)
    Bot.reply_to(message, "Howdy, how are you doing?")


@Bot.message_handler(commands=['inline'])
def send_welcome(message):
    inline_btns = telebot.types.InlineKeyboardMarkup()

    inline_btns.add(telebot.types.InlineKeyboardButton(text="Windows", url='http://microsoft.com'))
    inline_btns.add(telebot.types.InlineKeyboardButton(text="Linux", url='https://www.linuxfoundation.org/'))
    Bot.send_message(message.from_user.id, "Choose your destiny: ", reply_markup=inline_btns )


@Bot.message_handler(commands=['kb'])
def send_welcome(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
    button = telebot.types.KeyboardButton('button')
    keyboard.add(button)

    Bot.reply_to(message, "Howdy, how are you doing?", reply_markup=keyboard)


@Bot.message_handler(content_types=['text'])
def handle_command(message):
    print(message.text)
    # echo(message)
    smart_reply(message)


def random_typing(message):
    Bot.send_chat_action(message.from_user.id, "typing")
    time.sleep(random.randint(3, 6))


def smart_reply(message):
    if message.text == "button":
        random_typing(message)
        Bot.send_message(message.from_user.id, "Button Accepted!")

    if message.text == "Bots are fun":

        random_typing(message)
        Bot.send_message(message.from_user.id, "Indeed!")


def echo(message):
    Bot.send_message(message.from_user.id, message.text)


Bot.polling(none_stop=True, interval=0)