from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

# #Создание пустого поля в новом pdf файле
pdf_path = Path.cwd()/'New_PDF_file.pdf'
pdf_file = PdfFileWriter()#присваиваем объекту класс записи pdf
pdf_file.addBlankPage(width=72, height=72)#добавляем пустую область в объект рзамером 1 кв дюйм
with open(pdf_path, mode='wb') as new_pdf_file:#открываем файл с модом wb запись битов
    pdf_file.write(new_pdf_file) # метод .write  используется именно пакетом PyPDF2, !НЕ! pathlib

# #Извечение первой страницы
pdf_path_out = Path.cwd()/'Pride_and_Prejudice.pdf'
pdf_path_in = Path.cwd()/'New_PDF_1.pdf'
pdf_file_out = PdfFileReader(str(pdf_path_out))
page_0 = pdf_file_out.getPage(0)# получение 0 страницы из PDF файла
pdf_file_in = PdfFileWriter()
pdf_file_in.addPage(page_0)# добавления 0 страницы в объект PdfFileWriter
with pdf_path_in.open(mode='wb') as new_file:
    pdf_file_in.write(new_file)# запись файла