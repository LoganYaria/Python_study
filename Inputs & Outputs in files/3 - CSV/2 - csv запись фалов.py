import csv
import pathlib
file_path = pathlib.Path.cwd()/'example'/'temperatures_2.csv'
dialy_temperatures = [
    [68,65,68,70,74,72],
    [67,67,70,72,72,70],
    [68,70,74,76,74,73],
]

# # не пользуемся конструкцией with
# file = file_path.open(mode='w', encoding='utf-8',newline="")
# # создаем csv объект writer при помощи метода csv.writer
# writer = csv.writer(file)
# # при помощи метода .writerow() записывается список по строчно в файл
# for line in dialy_temperatures:
#     print(writer.writerow(line))
# file.close()

# # конструкция with
with file_path.open(mode='w', encoding='utf-8',newline='') as file:
    # for line in dialy_temperatures:
    #     print(csv.writer(file).writerow(line))
    # метод writerows для работы со списком списков
    print(csv.writer(file).writerows(dialy_temperatures))

