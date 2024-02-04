from PyPDF2 import PdfFileWriter
from pathlib import Path

pdf_path = Path.cwd()/'New_PDF_file.pdf'

pdf_file = PdfFileWriter()#присваиваем объекту класс записи pdf
pdf_file.addBlankPage(width=72, height=72)#добавляем пустую область в объект рзамером 1 кв дюйм
with open(pdf_path, mode='wb') as new_pdf_file:#открываем файл с модом wb запись битов
    pdf_file.write(new_pdf_file) # метод .write  используется именно пакетом PyPDF2, !НЕ! pathlib
