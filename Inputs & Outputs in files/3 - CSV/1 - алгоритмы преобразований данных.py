import pathlib

temperature_readings = [1,2,3,4,5,6]
file_path = pathlib.Path.cwd()/'example'/'temperatures.csv'
file_path.parent.mkdir(exist_ok=True)
file_path.touch()
with file_path.open(mode='w',encoding='utf-8') as file:
    file.write(str(temperature_readings[0]))
    for every_cell in temperature_readings[1:]:
        file.write(f',{every_cell}')
with file_path.open(mode='r',encoding='utf-8') as text:
    example_text = text.read()
example_text_list = example_text.split(',')
int_example_text_list = [ int(cell) for cell in example_text_list]
for every_cage in int_example_text_list:
    print(type(every_cage))