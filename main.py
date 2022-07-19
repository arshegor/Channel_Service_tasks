import threading
import argparse

from bot import sheet_bot
from back import back

if __name__ == "__main__":
    # Парсинг аргументов
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', help='database name', default="postgres")
    parser.add_argument('--keyfile', help='keyfile path', default="source/keys.json")
    parser.add_argument('--table', help='Google Sheet name', default="test")
    parser.add_argument('--user', help='username DB', default="postgres")
    parser.add_argument('--password', help='password DB', default="postgres")
    parser.add_argument('--host', help='host DB', default="localhost")
    parser.add_argument('--port', help='port DB', default="5432")
    parser.add_argument('--env', help='path to .env', default="")

    args = vars(parser.parse_args())
    
    # Запуск бота и бэка в разных потоках

    # Запуск двух модулей, если передан аргумент env
    if args["env"] != "":
        bot = threading.Thread(target=sheet_bot, args=(args["env"], args["database"], args["user"], args["password"], args["host"], args["port"]))
        back = threading.Thread(target=back, args=(args["database"], args["keyfile"],
                                                    args["table"], args["user"],
                                                    args["password"], args["host"], args["port"]))
        back.start(), bot.start()
        back.join(), bot.join()
    # Иначе запуск только модуля back
    else:
        back = threading.Thread(target=back, args=(args["database"], args["keyfile"],
                                                    args["table"], args["user"],
                                                    args["password"], args["host"], args["port"]))
        back.run()

    
