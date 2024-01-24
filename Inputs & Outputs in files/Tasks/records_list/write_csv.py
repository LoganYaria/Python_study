import csv
def writing_csv(file_dict,path_to_create):
    '''функция записывает список словарей в файл csv'''
    with path_to_create.open(mode='w',encoding='utf-8',newline='') as file:
        writer = csv.DictWriter(file,fieldnames=['name','score'])
        writer.writeheader()
        writer.writerows(file_dict)
