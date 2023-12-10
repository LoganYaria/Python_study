import pathlib
## Создание объекта Path
## 1 - из строк
path = pathlib.Path('D:/Work/PyCharm/Study/Fun/Fun/Inputs & Outputs in files/Hello.txt')
## или
path = pathlib.Path(r'D:\Work\PyCharm\Study\Fun\Fun\Inputs & Outputs in files\Hello.txt')

## 2 - Метод класса Path.home() и Path.cwd()
## Path.home создает объект Path содержащий путь к домашнему каталогу пользователя
home = pathlib.Path.home()
print(home)
## Path.cwd создает объект Path содержащий путь к текущему рабочему каталогу
work_catalog = pathlib.Path.cwd()
print(work_catalog)

## Оператор / (можно дополнить уже имеющийся Path)
home = pathlib.Path.home()
print(home)
aded_home = home/'Delete'/'Hello.txt'
print(aded_home)

## Абсолютные и относительные пути
## объявление
path = pathlib.Path('tuk/puk')
print(path)
print(path.is_absolute())#Функция is_absolute расскажет абсолютный ли путь в пазе
## Преобразование относительного пути абсолютный
home = pathlib.Path.home()
print((home/pathlib.Path('tuk/puk')).is_absolute())

## Path.resolve() поможет отыскать абсолютный путь
path = pathlib.Path('/Inputs & Outputs in files/Hello.txt')
absolute_path = path.resolve()
print(absolute_path)#работает неточно

