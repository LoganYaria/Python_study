#Класс длля чтения файла PDF
from PyPDF2 import PdfFileReader
from pathlib import Path

path_pdf = Path.cwd()/'Pride_and_Prejudice.pdf'

# #Открытие pdf
pdf = PdfFileReader(str(path_pdf)) # применяем класс к объекту
print(pdf.getNumPages()) # метод возвращает кол-во страниц
print(pdf.documentInfo)  # метод возвращает мета инфу о pdf документе

# #Извлечение текста из PDF

page_0 = pdf.getPage(0) # присваиваем объекту метод получения страницы
print(page_0.extractText()) # применяем метод извлечения текста объекта

# #Атрибут @.pages содержит список объектов, индексы которого равны странице
for page in pdf.pages:
    print(page.extractText())
