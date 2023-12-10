import pathlib

path_dep = pathlib.Path.cwd()/'new_directory_delete/file1.txt'
# #Создание каталогов и файлов для последующего удаления
# add_folders = [
#     path_dep.parent/'folder_d'/'File1.txt',
#     path_dep.parent/'folder_a'
#     ]
# for every_object in add_folders:
#     if every_object.parent.exists():
#         every_object.mkdir(exist_ok=True, parents=True)
#     else:
#         every_object.parent.mkdir(exist_ok=True, parents=True)
#     every_object.touch(exist_ok=True)
# # Перемещение файла при  old_path.replace(new_path)
# path_appr = pathlib.Path.home()/'new_directory_delete/Folder_a/file1.txt'
# if not path_appr.exists():
#     print(path_dep.replace(path_appr))
# print(path_appr.replace(path_dep))

# #@ЛИШНЕЕ
# path_dep.parent.mkdir(exist_ok=True, parents=True)
# path_dep.touch()

# #Переименование каталога
# path_dep = pathlib.Path.home()/'new_directory_delete/Folder_c'
# path_dest = pathlib.Path.home()/'new_directory_delete/Folder_d'
# if not path_dest.exists():
#     print(path_dep.replace(path_dest))

# #Удаление фалов .unlink() /missing_ok=True не вызовет ошибку в случае если файл уже удален
# file_to_delete = path_dep.parent/'program1.py'
# #file_to_delete.touch()
# file_to_delete.unlink(missing_ok=True)
# print(file_to_delete.exists())
# for every_path in file_to_delete.parent.iterdir():
#     print(every_path)

# #Удaление каталогов .rmdir() !команда удаляет только пусты папки
# directory_to_delete = path_dep.parent/'folder_a'
# print(directory_to_delete.rmdir())

#Пример удаления каталога с файломи внутри
#
# for every_path in (path_dep.parent/'folder_d').iterdir():
#     every_path.unlink()#missing_ok=True)
# (path_dep.parent/'folder_d').rmdir()

# #Удаление при помощи модуля shutil

# import shutil
# shutil.rmtree(path_dep.parent/'folder_d')
