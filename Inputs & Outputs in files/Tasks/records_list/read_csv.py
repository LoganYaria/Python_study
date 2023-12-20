import pathlib
import csv
def read_csv_fun():
    file_path = pathlib.Path.cwd()/'practice_files/scores.csv'
    score_list = []
    dump_line =[]
    with file_path.open(mode='r', encoding='utf-8', newline='') as file:
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
    sorted_scored_list = sorted(score_list, key=lambda x: x['score'], reverse=True)
    return(sorted_scored_list)
