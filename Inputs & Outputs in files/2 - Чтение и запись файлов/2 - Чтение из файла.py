import pathlib

path  = pathlib.Path.cwd()/'hello.txt'
with path.open(mode='r',encoding='utf-8') as file:
    # # Cтандартное чтение с помощью функции .read()
    # text = file.read()
    # print(text)
    # print(type(text))

    # # функция .readlines()    end='' убирает вывод переноса строки после каждой строки файла.
    for line in file.readlines():
        print(line, end='')




#фунция readline  - читает текст посимфольно