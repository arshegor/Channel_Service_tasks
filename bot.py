import telebot
import os

from time import sleep
from datetime import date
from telebot import types
from db import connect_to_db, get_table_db
from dotenv import load_dotenv

def sheet_bot(env_path="source/.env", database="arshegor", 
                user="", password="", host="localhost", port="5432"):
    # Подгрузка токена бота
    load_dotenv(dotenv_path=env_path)
    TOKEN = os.getenv("TOKEN")

    # Подключение к БД
    _, cursor = connect_to_db(database=database, user=user, password=password, host=host, port=port)

    # Создание бота
    bot = telebot.TeleBot(TOKEN)
    print(111)
    # Декоратор обработки команды /start
    @bot.message_handler(commands=['start'])
    def notificate(message):
        while True:
            data = get_table_db(cursor=cursor)
            late_message = "Просроченные заказы:\n____________ \n"
            for row in range(len(data)):
                try:
                    # Условие проверяющее просрочку заказа относительно сегодняшей даты
                    if date.fromisoformat(data[row][3]) < date.today():
                        late_message += f'Заказ: {data[row][1]}\nСрок поставки: {data[row][3]}\n____\n'
                except:
                    continue

            if late_message == "Просроченные заказы:\n____________ \n":
                bot.send_message(message.chat.id, "Просроченных заказов не найдено")
            else:
                bot.send_message(message.chat.id, late_message)
            # Отправка 1 раз в час
            sleep(3600)
        

    bot.infinity_polling()

