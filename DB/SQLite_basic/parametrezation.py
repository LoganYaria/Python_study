import sqlite3

enter_first_name = input('Enter first name: ')
enter_second_name = input('Enter second name: ')
enter_age = int(input('Enter Age: '))

data = (enter_first_name, enter_second_name, enter_age)

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    cursor.execute('INSERT INTO People VALUES(?,?,?)', data) #Используй параметризацию для корректного ввода данных
    cursor.execute( #  А также для обновления данных
        "UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;",
        (76, enter_first_name,enter_second_name)
    )
    # Irrational job
    # query = f"INSERT INTO People VALUES('{enter_first_name}','{enter_second_name}',{enter_age})"
    # cursor.execute(query)

    query = f"SELECT * FROM People WHERE FirstName like '%{enter_first_name}%'"
    result = cursor.execute(query)
    row = result.fetchone()
    print(row)