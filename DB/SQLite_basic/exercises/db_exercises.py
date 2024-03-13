import sqlite3

sql_script = ("""
DROP TABLE IF EXISTS Roster;
CREATE TABLE Roster(Name TEXT, Species TEXT, Age INT);
""")

data = (
    ('Benjamin Sisko','Human',40),
    ('Jadzia Dax','Trill',300),
    ('Kira Nerys','Bajoran',29)
)

select = "SELECT Name,Age FROM Roster WHERE Species like '%Bajoran%'"

with sqlite3.connect('exercises_db.db') as connection:
    cursor = connection.cursor()
    cursor.executescript(sql_script)
    cursor.executemany("INSERT INTO Roster VALUES(?,?,?);", data)
    cursor.execute("UPDATE Roster SET Name=? WHERE Species=?;",('Erzi Dax','Trill'))
    result = cursor.execute(select)
    rows = result.fetchall()
    print(rows)