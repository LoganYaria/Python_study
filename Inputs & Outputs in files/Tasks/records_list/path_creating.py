import pathlib

def import_path():
    '''функция позволяет ввести путь к файлу формата csv, откуда выкачает данные.'''
    import_approved_path = pathlib.Path('test')
    while not (import_approved_path.exists() and import_approved_path.is_file() and import_approved_path.suffix == '.csv'):
        not_approved_path = input('Enter path to csv with scores: ')
        import_approved_path = pathlib.Path(not_approved_path)
    return import_approved_path


def export_path():
    '''функция позволяет ввести путь к файлу формата csv, откуда выкачает данные.'''
    export_approved_path = pathlib.Path('test/xuest')
    while not (export_approved_path.parent.exists() and export_approved_path.suffix == '.csv'):
        not_approved_path = input('Enter path to csv with scores and new file: ')
        export_approved_path = pathlib.Path(not_approved_path)

    export_approved_path.touch()
    return export_approved_path
