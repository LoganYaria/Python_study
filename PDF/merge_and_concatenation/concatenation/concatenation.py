from PyPDF2 import PdfFileMerger
from pathlib import Path

reports_dir = Path.cwd()/'expense_reports' #путь к папке с кучей пдф
reports_path = []
for obj in reports_dir.glob('*.pdf'): #поиск пдфок в папке
    reports_path.append(obj) #пихание пдфок в список
reports_path.sort #сортировка

# for name in reports_path:
#     print(name.name)

concatenate_file = PdfFileMerger() # создания объекта с вохожностью конкатенации
for path in reports_path: #перебор путей с пдфками
    concatenate_file.append(str(path)) #конкатенация пдфок в объект через строку

out_file_path = Path.cwd()/'Concatenate_PDF.pdf' # запись объекта в файл пдф
with out_file_path.open(mode='wb') as file:
    concatenate_file.write(file)