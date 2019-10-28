import telebot
import time
import random

Bot = telebot.TeleBot("957417052:AAHLnkugOejglnzeY5141FahYxxYcuhOjyE")


@Bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    RandomTyping(message)
    Bot.reply_to(message, "Howdy, how are you doing?")


@Bot.message_handler(commands=['inline'])
def send_welcome(message):
    inlineBtns = telebot.types.InlineKeyboardMarkup()

    inlineBtns.add(telebot.types.InlineKeyboardButton(text="Windows", url='http://microsoft.com'))
    inlineBtns.add(telebot.types.InlineKeyboardButton(text="Linux", url='https://www.linuxfoundation.org/'))
    Bot.send_message(message.from_user.id, "Choose your destiny: ", reply_markup=inlineBtns )

@Bot.message_handler(commands=['kb'])
def send_welcome(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
    button = telebot.types.KeyboardButton('button')
    keyboard.add(button)

    Bot.reply_to(message, "Howdy, how are you doing?", reply_markup=keyboard)


@Bot.message_handler(content_types=['text'])
def handle_command(message):
    print(message.text)
    #Echo(message)
    SmartReply(message)

def ShowKeyboard():
    pass


def RandomTyping(message):
    Bot.send_chat_action(message.from_user.id, "typing")
    time.sleep(random.randint(3, 6))


def SmartReply(message):
    if message.text == "button":
        RandomTyping(message)
        Bot.send_message(message.from_user.id, "Button Accepted!")

    if message.text == "Bots are fun":

        RandomTyping(message)
        Bot.send_message(message.from_user.id, "Indeed!")

def Echo(message):
    Bot.send_message(message.from_user.id, message.text)



Bot.polling(none_stop=True, interval=0)