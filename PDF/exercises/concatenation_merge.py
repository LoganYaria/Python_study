from pathlib import Path
from PyPDF2 import PdfFileMerger

files_nums_path = Path.cwd()/'exercises_dir'
path_list = []

for path in files_nums_path.glob('*[1,2].pdf'):
    path_list.append(str(path))

concatenated_file = PdfFileMerger()
concatenated_file_path = Path.cwd()/'exercises_dir'/'concatenated.pdf'
for sting in path_list:
    concatenated_file.append(sting)
with concatenated_file_path.open(mode='wb') as file:
     concatenated_file.write(file)


for obj in files_nums_path.glob('*3.pdf'):
    merging_file_path=str(obj)
merging_file = PdfFileMerger()
merging_file.append(str(concatenated_file_path))
merging_file.merge(1,str(merging_file_path))
merged_file_path = files_nums_path/'Merged.pdf'
with merged_file_path.open(mode='wb') as file:
    merging_file.write(file)