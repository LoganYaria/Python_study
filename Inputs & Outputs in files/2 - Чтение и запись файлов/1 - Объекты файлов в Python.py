import pathlib
# Создание файловых объектов
# Метод Path.open() (возвращает новый файловый объект от path)
path = pathlib.Path.cwd()/'hello.txt'
path.touch()
file = path.open(mode='r', encoding='utf-8')
print(file)
file.close # закрывет файл
# вариации ключа mode = {
#     'r'  : 'для чтения текстового файла + ошибка, если не удалось открыть',
#     'w'  :'для записи текстового файла и перезаписывает при записи',
#     'a'  :'для присоединении данных в конец текстового файла',
#     'rb' : 'для чтения двойичного файла + ошибка, если не удалось открыть',
#     'wb' : 'для записи двоичного файла и перезаписывает при записи',
#     'ab' : 'для присоединении данных в конец двоичного файла',
# }
# вариации кодировок encoding = {
#     'ascii' : 'ASCII',
#     'utf-8'  : 'UTF-8',
#     'utf-16': 'UTF-16',
#     'utf-32': 'UTF-32',
# }

# функция open()
file_path = r'E:\WORK\PyCharm\Fun\Inputs & Outputs in files\2 - Чтение и запись файлов\hello.txt'
file = open(file_path, mode='r', encoding='utf-8')
print(file)
file.close()

# Команда with позволяет закрыть файл, даже если до закрытия файла произошла ошибка
# Работа с методом.open()
with path.open(mode='r', encoding='utf-8') as file:
    print(file) # Код с отступом работает с открытым файлом

# Работа с функцией open()
with open(file_path, mode='r', encoding='utf-8') as file:
    print(file)