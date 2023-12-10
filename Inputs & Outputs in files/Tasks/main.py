#main
import path_checking
import filter_of_files
import move_of_files

list_of_path_for_moving = filter_of_files.filtering(path_checking.checking_source_path())#вызов поиска по корневому пути

for every_object in list_of_path_for_moving:#логирование пути к объектам
    print(every_object)

move_of_files.moving(list_of_path_for_moving,path_checking.checking_destinatioon_path())#перемещение найденных файлов в необходимый каталог
