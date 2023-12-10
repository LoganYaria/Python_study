#filter_of_files
def filtering (path_for_filtering):
    '''Возвращает все пути с файлами раширения "jpg"  "png" "gif" c проверкой на наличие файла'''
    list_of_paths = []
    for every_path_png in path_for_filtering.glob('**/*.png'):
        list_of_paths.append(every_path_png)
    for every_path_jpg in path_for_filtering.glob('**/*.jpg'):
        list_of_paths.append(every_path_jpg)
    for every_path_gif in path_for_filtering.glob('**/*.gif'):
        list_of_paths.append(every_path_gif)

    for every_path_general in list_of_paths:
        if not every_path_general.is_file():
            list_of_paths.pop(list_of_paths.index(every_path_general))

    return list_of_paths