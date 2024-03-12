import sqlite3

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    creator = "CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);" # создаем таблицу
    inserter = "INSERT INTO People VALUES('Ron','Wisley',17);" # инсертим данные
    cursor.execute(creator)
    cursor.execute(inserter)
# # Не нужен коммит если используешь with
    query = "SELECT * FROM people;"
    result = cursor.execute(query)
    row = result.fetchone()
    print(row[0])
