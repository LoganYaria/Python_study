class ManagedFile:
    def __str__(self):
        return 'Пример использования context manager в записи файлов'
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Пример использования context manager через библиотеку contextlib
from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        f = open(name, mode='w')
        yield f
    finally:
        f.close()



# Пример изменения файла
#file_path = r'E:\WORK\PyCharm\Python_study\Context Manager\simple_write.txt'
file = open('simple_write.txt', mode='w', encoding='utf-8')
file.write("It's simple write!")
file.close()

# Пример использования менеджера контекста в библиотеке pathlib
import pathlib
path = pathlib.Path.cwd()/'pathlib_write.txt'
with path.open(mode='w', encoding='utf-8') as write_file:
    write_file.write("It's pathlib write!")
with path.open(mode='r', encoding='utf-8') as read_file:
    print(read_file.read())

# Пример использхования менеджера контекста через класс
with ManagedFile('managed_by_class_write.txt') as f:
    f.write("It's managed context write by class!")

# Пример использования менеджера констекста через декоратор-генератор
with managed_file('meneged_by_contextlib.txt') as f:
    f.write("It's managed context write by contextlib generator-decorator!")
