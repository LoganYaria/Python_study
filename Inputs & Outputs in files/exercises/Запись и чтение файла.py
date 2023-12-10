import pathlib
text_to_write = [
    'Discovery\n',
    'Enterprise\n',
    'Defiant\n',
    'Voyager\n',
]

path_to_file = pathlib.Path.cwd()/'wrt_rd_dir'/'starships.txt'
path_to_file.parent.mkdir(exist_ok=True)
path_to_file.touch()
with path_to_file.open(mode='w', encoding='utf-8') as file:
    for every_line in text_to_write:
        file.write(every_line)
with path_to_file.open(mode='r', encoding='utf-8') as file:
    for every_line in file.readlines():
        if every_line[0] =='D':
            print(every_line, end='')
