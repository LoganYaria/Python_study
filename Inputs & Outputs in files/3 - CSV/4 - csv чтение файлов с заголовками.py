import pathlib
import csv

file_path = pathlib.Path.cwd()/'example/employees.csv'
# # # чтение csv через открытие
# file = file_path.open(mode='r',encoding='utf-8',newline='')
# # # создаем объект csv DictReader (словарь) на базе открытого созданного объекта file
# reader = csv.DictReader(file)
# # # aтрибут .fieldnames содержит список имен csv
# print(reader.fieldnames)
# for line in reader:
#     print(line)
# file.close()

def procee_row(row):
    row['salary'] = float(row['salary'])
    return row

with file_path.open(mode='r',encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        procee_row(row)
        print(row)
        print(type(row['salary']))