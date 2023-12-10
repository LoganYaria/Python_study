import pathlib

path = pathlib.Path.cwd()/'hello.txt'

lines_of_text = [
    'if you 555, then I\'m 333\n',
    'if you 555, then I\'m 333\n',
    'if you 555, then I\'m 333'
]
#  # Обычная запись в файл
with path.open(mode='w', encoding='utf-8') as file:
    file.write('Hello, moto')

# # Запись нескольких строк
with path.open(mode='w', encoding='utf-8') as file:
        file.writelines(lines_of_text)
with path.open(mode='r', encoding='utf-8') as file:
    print(file.readlines())

# # Так как mode='a' запсиь будет добавлена в конец текста
with path.open(mode='a', encoding='utf-8') as file:
    file.write('\nGood bye, moto(((')
with path.open(mode='r', encoding='utf-8') as file:
    print(file.read())
    # for every_line in file.readlines():
    #     print(every_line,end='')

#Если не уверенности в том, что путь существует, можно применить конструкцию
path.parent.mkdir(exist_ok=True, parents=True)
with path.open(mode='w',encoding='utf-8') as file:
    file.write('конструкцияб бро, конструкция!')