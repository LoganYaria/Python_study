from pathlib import Path
from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_export_path = Path.cwd()/'files'/'ugly.pdf'
pdf_import_path = Path.cwd()/'files'/'correct_ugly.pdf'
pdf_import_path_1 = Path.cwd()/'files'/'correct_ugly_1.pdf'
pdf_read_file = PdfFileReader(str(pdf_export_path)) # читаем pdf
pdf_write_file = PdfFileWriter()

for page_num in range(pdf_read_file.getNumPages()):
    export_page = pdf_read_file.getPage(page_num) # вытаскиваем страницу из читательного файла
    if page_num % 2 == 0: # проверка четности
        export_page.rotateClockwise(361) # поворот по часовой стрелке . только %90гр. Против часовой - rotateCounterClockwise
    pdf_write_file.addPage(export_page)

with pdf_import_path.open(mode='wb') as file:
    pdf_write_file.write(file)


# Второй способ

pdf_read = PdfFileReader(str(pdf_export_path))
print(pdf_read.getPage(0)) # Вывод словаря значений, содержащий метаданные о странице
page = pdf_read.getPage(0) # Объекту присваивается метод
print(page['/Rotate']) #вывод свойства /Rotate
page.rotateClockwise(90)
print(page['/Rotate'])

for page in range(pdf_read_file.getNumPages()):
    page_obj = pdf_read_file.getPage(page)# метод getPage присвиавется объекту класса PdfFileReader
    if page_obj['/Rotate'] == (-90): # проверка есть ли поворот страницы против часовой стрелы
        page_obj.rotateClockwise(90) # если есть, то повернуть обратно
    pdf_write_file.addPage(page_obj) # и записать

with pdf_import_path_1.open(mode='wb') as file:
    pdf_write_file.write(file)
