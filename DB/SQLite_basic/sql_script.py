import sqlite3

# # Сам скрипт:
sql_script = '''
DROP TABLE IF EXISTS People;
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
INSERT INTO People VALUES("Ron","Wisley",17);
'''

# # Кортеж значений для инсерта
insert_values = (
    ("Harry", "Potter", 17),
    ("Harmoni", "Granger", 17),
    ("Draco", "Malfoy", 17),
)

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    cursor.executescript(sql_script) # executescript выполняет несколько команд
    cursor.executemany("Insert into People VALUES(?,?,?)", insert_values) # executemany можно испоользовать
# # когда есть несколько значений вставки


    query = "Select * from people;"
    result = cursor.execute(query)
    row = result.fetchone()
    print(row)