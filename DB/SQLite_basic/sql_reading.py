import sqlite3
from pathlib import Path
import csv

row_list=[]
query = "SELECT * FROM People;"

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    result = cursor.execute(query)
    rows = result.fetchall() # ВЫВОДИТ КОРТЕЖ КОРТЕЖЕЙ ПОДХОДЯЩИХ ЗАПИСЕЙ

for line in rows:
    row_list.append(list(line))
print(row_list)


path_csv = Path.cwd()/'new_csv.csv'

with path_csv.open(mode='w',encoding='utf-8',newline="") as file:
    for row in row_list:
        csv.writer(file).writerow(row)