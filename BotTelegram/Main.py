
import telebot

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

API = "5910116610:AAHiRBYEf9KkPzsNoACoSz0JY4UygqlIQqA"
bot = telebot.TeleBot(API)

def start(menssagem):
    if menssagem.document is True:
        return True

@bot.message_handler(func=start)
def handle_command_adminwindow(message):
        bot.send_message(chat_id=message.chat.id,
                         text="Olá "+message.chat.first_name+" "+"Vamos à primeira pergunta: \n",
                         parse_mode='HTML')

bot.polling()