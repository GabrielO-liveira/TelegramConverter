import ast
import telebot
from telebot import types
import sqlite3

conn = sqlite3.connect("C:\Program Files (x86)\DB Browser for SQLite\Telegram.db", check_same_thread=False)
API = "5910116610:AAHiRBYEf9KkPzsNoACoSz0JY4UygqlIQqA"
bot = telebot.TeleBot(API)
cursor = conn.cursor()

cont =1
id= str(cont)


for Opcao1 in cursor.fetchall():
    Bt1 = {"a)": Opcao1, "b)": "", "c)": "", "d))": "  "}


def makeKeyboard():
        markup = types.InlineKeyboardMarkup()
        for key, value in Bt1.items():
            markup.add(types.InlineKeyboardButton(text=value, callback_data="['value', '" + value + "', '" + key + "']"))
        return markup


for Pergunta in cursor.fetchall():
    @bot.message_handler(commands=['play'])
    def handle_command_adminwindow(message):
        bot.send_message(chat_id=message.chat.id, text=Pergunta, reply_markup=makeKeyboard(), parse_mode='HTML')


cursor.execute("SELECT Correta FROM Perguntas WHERE id ="+ id +"")
for Correta in cursor.fetchall():
        @bot.callback_query_handler(func=lambda call: True)
        def handle_query(call):
             if call.data.startswith("'value'"):
                 Value_Button = ast.literal_eval(call.data)[1]
                 Value_Button = tuple(map(int, Value_Button.split(' ')))
             if Correta == Value_Button:
                  bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Resposta correta")
                  cont+1
                  makeKeyboard()
             else:
                 bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Resposta incorreta tente novamente")
bot.polling()
