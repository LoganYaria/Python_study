import pathlib
import csv
numbers = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
]
empty_numbers = []
favorite_colors = [
    {'name':'Joe','favorite_color':'blue'},
    {'name':'Anne','favorite_color':'green'},
    {'name':'Bailey','favorite_color':'red'},
]
empty_favorite_colors = []
file_path = pathlib.Path.cwd()/'wrt_rd_dir/numbers.csv'
file_path_2 = pathlib.Path.cwd()/'wrt_rd_dir/favorite_colors.csv'

# # Запись
# # with file_path.open(mode='w',encoding='utf-8',newline='') as file:
# #     writer = csv.writer(file).writerows(numbers)
# # Чтение
# with file_path.open(mode='r',encoding='utf-8', newline='') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             int_line = [int(element) for element in row]
#             empty_numbers.append(int_line)
# print(empty_numbers)
# # Запись с заголовками
# with file_path_2.open(mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file,fieldnames=(['name','favorite_color']))
#     print(writer.writeheader())
#     print(writer.writerows(favorite_colors))
# # Запись с заголовками
with file_path_2.open(mode='r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        empty_favorite_colors.append(row)

print(empty_favorite_colors)
