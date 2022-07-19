import gspread

from exchange_rate import get_rate, convert_valute
from db import connect_to_db, insert_row, get_table_db, clear_table_db

# Получение данных из Google таблицы
def get_table(filename, table):
    # Подключаемся к API при помощи файла-ключа
    gc = gspread.service_account(filename=filename)

    #Открываем тестовую таблицу
    sh = gc.open(table)

    # Получаем все строки таблицы
    return sh.sheet1.get()


# Конвертация даты в формат ГГ:ММ:ДД для корректной записи в БД
def date_to_YMD(date):
    date = date.split(".")
    return date[2] + "-" + date[1] + "-" + date[0]


# Адаптация гугл таблицы для записи в БД
def adapt_for_database(table):
    # Убираем первую строку с названиями колонок из таблицы 
    table.pop(0)
    for row in range(len(table)): 
        try:
            # Конвертируем дату п, конвертируем доллары в рубли
            table[row][3] = date_to_YMD(table[row][3])

            # Переводим стоимость в банковский вид
            table[row][2] = str(float(table[row][2]))

            # Рассчитываем стоимость в рублях и добавляем в строку полученной таблицы
            table[row].append(str(convert_valute(float(table[row][2]), get_rate())))
        except:
            # Если данные оказались некорректными, оставляем заказ пустым, 
            # тк все данные должны быть в таблице
            table[row] = [None, None, None, None, None]
        
        # Перевод строки таблицы из списка в кортеж 
        # для ускорения и удобства записи в БД
        table[row] = tuple(table[row])
    return table


def back(database="postgres", keyfile="source/keys.json", 
        table_name="test", user="postgres", 
        password="", host="localhost", port="5432"):
    # Подключение к БД
    try:
        conn, cursor = connect_to_db(database=database, user=user, password=password, host=host, port=port)
        print("Connect to DB – OK")
    except:
        print("Connect to DB – FALSE")

    while True:
        table = get_table(keyfile, table_name)
        print("Get Google table – OK")

        db_table = get_table_db(cursor)
        print("Get PostgreSQL table – OK")

        data = adapt_for_database(table)
        print("Table adapted")

        # Если данные в Google таблице не совпадают с данными в таблице БД,
        # то перезапись таблицы БД
        if db_table != data:
            print("Found changes")

            # Очищаем таблицу
            clear_table_db(conn, cursor)

            # Записываем новые данные в БД
            for d in data:
                insert_row(d, conn, cursor)
            print("Insert DONE")