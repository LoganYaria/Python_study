#move_of_files
def moving (source_path, destination_path):
    '''Перемещение из файлов типа "jpg"  "png" "gif", найденных из заданного каталога в указанный каталог'''
    for every_souce_path in source_path:
        print(every_souce_path.replace(destination_path/every_souce_path.name))