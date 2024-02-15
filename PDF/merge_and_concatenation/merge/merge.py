from pathlib import Path
from PyPDF2 import PdfFileMerger

path_report = Path.cwd()/'quarterly_report'#общий путь
report_file_path = path_report/'report.pdf'#путь к репорту
toc_file_path = path_report/'toc.pdf'#путь к оглавлению

full_report = PdfFileMerger()#объявление объекта
full_report.append(str(report_file_path))#добавление в объект репорт
full_report.merge(1, str(toc_file_path))#вставк пути оглавления в обхект репорта

full_report_path = Path.cwd()/'Full_report.pdf'#запись
with full_report_path.open(mode='wb') as file:
    full_report.write(file)