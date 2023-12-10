import pathlib
path = pathlib.Path.home()/'Delete'/'hello.txt'
path_2 = pathlib.Path('/Parrot/Petya')

# .parents - вернет список каталогов полного пути в обратном напрвлении (list)
print(list(path.parents))
for directory in path.parents:
    print(directory)

# .parent выведет весь путь
print(path.parent)

# Если путь явл абсолютным, то можно обратиться в корень .anchor (string)
print(path.anchor)

# Для относительных путей вернет пустую строку
print(path_2.anchor)

# .name указывает имя файла/каталога, на который указывает путь.
print(path.name)
print(path_2.name)

# Hello.txt - .stem вернет Hello / ./suffix вернет .txt
print(path.stem)
print(path.suffix)

# .exists вернет ответ существует ли файл/катлог на саомо деле в нашем path
print(path.exists())
print(path_2.exists())

# .is_file вернет  ответ ведет ли путь к файлу (работает по принципу .exist)
print(path.is_file())

# .is_dir() вернет  ответ ведет ли путь к директории (работает по принципу .exist)
print(path.is_dir())
