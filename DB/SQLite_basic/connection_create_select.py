import sqlite3
#
# connection = sqlite3.connect('test_database.db') # заюзав эту функцию, Py будет искать db c таким назв. в текущем dir,
# # #  если не найдет, то создаст в текущем каталоге. Если нужен другой каталог, нужно указать полный путь
# # # connection = sqlite3.connect(':memory:') # исп для создания db  в памяти, пока работает программа.
#
# print(type(connection))
#
# cursor = connection.cursor()
# print(type(cursor)) # курсор есть окно для взаимодействия  проги с db. При помощи него можно создавать таблицы, выполнять
# # # команды sql и получать результаты запросов
#
# #Использование функции SQLite datetime()
# query = "SELECT datetime('now','localtime')" # SQL команда, возврашающая текущую дату\время
# result = cursor.execute(query) # тоже объект курсор
# print(result)
# row = result.fetchone() # fetchone() - метод возвращает кортеж с первой строкой результатов
# print(row)
# time = row[0]
# print(time)
# connection.close()

# # Работа при помощи with

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now','localtime')"
    result = cursor.execute(query)
    row = result.fetchone()
    time = row[0]
    print(time)