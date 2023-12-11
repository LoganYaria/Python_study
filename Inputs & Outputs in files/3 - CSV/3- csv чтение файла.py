import pathlib
import csv

file_path = pathlib.Path.cwd()/'example'/'temperatures_2.csv'
daily_temperatures = []

with file_path.open(mode='r', encoding='utf-8', newline='') as line:
    for every_row in (csv.reader(line)):
        int_line = [int(every_number) for every_number in every_row]
        daily_temperatures.append(int_line)
print(daily_temperatures)