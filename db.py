import psycopg2

# Подклбчение к базе 
def connect_to_db(database="postgres", user="", password="", host="localhost", port="5432"):
    conn = psycopg2.connect(database=database,
                        user=user,
                        password=password,
                        host=host,
                        port=port)
    cursor = conn.cursor()
    return conn, cursor

# Получение всей таблицы
def get_table_db(cursor):
    cursor.execute("SELECT * FROM public.test")
    db_table = cursor.fetchall()

    # Перевод всех полученных данных в кортежи
    for i, (id, order, cost_d, date, cost_r) in enumerate(db_table):
        # Если встречаются пустые ячейки – устанавливаем None
        if id == None or order == None or cost_d == None or date == None or cost_r == None:
            db_table[i] = (None,None,None,None,None)
        else:
            # Если есть данные – переводим в строки
            db_table[i] = (str(id), str(order), str(cost_d), str(date), str(cost_r))

    return db_table


# Очитска таблицы через TRUNCATE для ускорения (DELETE работает медленнее)
def clear_table_db(conn, cursor):
    cursor.execute("TRUNCATE public.test")
    conn.commit()


# Запись строки в таблицу БД
def insert_row(data, conn, cursor):
    cursor.execute("INSERT INTO public.test (id, order_num, cost_dollar, delivery_date, cost_rub) VALUES (%s, %s, %s, %s, %s)", data)
    conn.commit()
   









