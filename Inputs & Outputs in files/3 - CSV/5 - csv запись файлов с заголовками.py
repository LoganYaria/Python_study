import pathlib
import csv

people=[
    {'name':'Veronica', 'age':30},
    {'name':'Andrew', 'age':33},
    {'name':'Sam', 'age':40},
]

file_path = pathlib.Path.cwd()/'example/people.csv'

file = file_path.open(mode='w',encoding='utf-8',newline='')
# # метод DictWriter исп. для записи с заголовками
writer = csv.DictWriter(file,fieldnames=['name','age'])
# # writeheader() метод writehead запишет заголовки в начале файла
print(writer.writeheader())
# # writerow метод запишет построчно, а writerows() метод запишетцеликом весь словарь
print(writer.writerows(people))
file.close
#