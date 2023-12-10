import pathlib
## Создание каталога
# new_directory = pathlib.Path.home()/'new_directory_delete'
## exist_ok = True - не приведет к ошибке, если каталог уже создан
# new_directory.mkdir(exist_ok = True)

## Создание каталога в несуществующей папке приводит к ошибке
#nested_dir = new_directory/'Folder_a/Folder_b'
## parents = True - используется для создания подительских подкаталогов до создания каталога
#nested_dir.mkdir(exist_ok = True, parents = True)
## как варик перехватить ошибку и предложить ввести корректный уже существующий путь

## Cоздание файла
## Если попытаться создать уже созданный файл, ошибки не будет
## Создать файл в несуществующей дериктории невозможно
# file_path = new_directory/'file.txt'
# print(file_path.exists())
# file_path.touch()
# print(file_path.exists())
# print(file_path.is_file())

## Создание файла в еще несуществуемом каталоге
# file_path = new_directory /'Folder_c/file.txt'
# file_path.parent.mkdir(exist_ok = True, parents = True)
# file_path.touch()
