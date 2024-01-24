import csv
def read_csv_fun(path_to_read):
    score_list = []
    with path_to_read.open(mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        for line in reader:
            line['score'] = int(line['score'])
            if len(score_list) == 0:
                score_list.append(line)
            for element in score_list:
                if line['name'] == element['name']:
                    if line['score'] > element['score']:
                        element['score'] = line['score']
                else:
                    score_list.append(line)
                break
    sorted_scored_list = sorted(score_list, key=lambda x: x['score'], reverse=True)# Сортировка словаря по score по убыванию
    return(sorted_scored_list)
