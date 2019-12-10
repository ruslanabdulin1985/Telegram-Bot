import telebot
import random
import time

Bot = telebot.TeleBot("1061779174:AAEv7oAZa11E0hUx_Qa1ZHHd6ogS2_Xd7AA")


@Bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    Bot.reply_to(message, "Howdy, how are you doing?")


@Bot.message_handler(content_types=['text'])
def send_welcome(message):
    inline_btns = telebot.types.InlineKeyboardMarkup()

    inline_btns.add(telebot.types.InlineKeyboardButton(text="Microsoft", url='http://microsoft.com'))
    inline_btns.add(telebot.types.InlineKeyboardButton(text="Linux", url='https://www.linuxfoundation.org/'))
    Bot.send_message(message.from_user.id, "Choose your destiny: ", reply_markup=inline_btns)


def random_typing(message):
    Bot.send_chat_action(message.from_user.id, "typing")
    time.sleep(random.randint(3, 6))


Bot.polling(none_stop=True, interval=0)