import pathlib


def checking_source_path():
    '''функция ввода и проверки корректности введенного пути'''
    approved_source_path = pathlib.Path('Test')

    while not (approved_source_path.exists() and approved_source_path.is_dir()):
        not_approved_source_path = input('Enter the path to the directory from which images will be searched: ')
        approved_source_path = pathlib.Path(not_approved_source_path)

    return approved_source_path

def checking_destinatioon_path():
    '''функция ввода и проверки корректности введенного пути'''
    approved_destination_path = pathlib.Path('Test')

    while not (approved_destination_path.exists() and approved_destination_path.is_dir()):
        not_approved_destination_path = input('Enter the path to the directory where the images will be destined: ')
        approved_destination_path = pathlib.Path(not_approved_destination_path)

    return  approved_destination_path