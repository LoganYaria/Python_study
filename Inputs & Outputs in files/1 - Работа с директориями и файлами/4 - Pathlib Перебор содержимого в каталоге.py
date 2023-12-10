import pathlib
# # .iterdir перечислит все объекты, находящиеся  в пути
new_directory = pathlib.Path.home()/'new_directory_delete'
print(list(new_directory.iterdir()))
# или
for every_object in new_directory.iterdir():
    print(every_object)

# Поиск файлов в каталоге
# .glob вернет все пути, что найдет в опр каталоге
# * - сколько угодно симфолов до искомого
# ? - один символ до искомого
# [CB] - один из символов, перечисленных в квадратных скобках
for every_object in new_directory.glob('*.txt'):
     print(every_object)

# Пример того, как можно нагенерить всякой хероты
paths = [
    new_directory / 'program1.py',
    new_directory / 'program2.py',
    new_directory / 'folder_a' / 'program3.py',
    new_directory / 'folder_a' / 'folder_b'/ 'image1.jpg',
    new_directory / 'folder_a' / 'folder_b'/ 'image2.png',
]
for every_path in paths:
    every_path.touch()
# использование символа *
for every_object in new_directory.glob('*.py'):
    print(every_object)
for every_object in new_directory.glob('*1*'):
    print(every_object)

# использование символа ?
for every_object in new_directory.glob('program?.py'):
    print(every_object)
for every_object in new_directory.glob('?older_?'):
    print(every_object)
for every_object in new_directory.glob('*1.??'):
    print(every_object)

# использование символов []
for every_object in new_directory.glob('program[21567].py'):
    print(every_object)

# использование символа ** (поиск по всему Path)
print(list(new_directory.glob('**/*py')))
# или функция .rglob()
print(list(new_directory.rglob('*py')))