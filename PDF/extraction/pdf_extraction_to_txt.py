# #Извлечение pdf файла в txt файл
from pathlib import Path
from PyPDF2 import PdfFileReader
# #Обозначение путей
pdf_path = Path.cwd()/'Pride_and_Prejudice.pdf'
txt_path = Path.cwd()/'PrIdE_AnD_PrEjUdIcE.txt'
# #Работа с пакетом PyPDF2
pdf = PdfFileReader(str(pdf_path))
title = pdf.documentInfo.title
num_pages = pdf.getNumPages()
# #Работа с извлечением
with txt_path.open(mode='a',encoding='utf-8',newline='') as txt_file:
    txt_file.write(f'{title}\nNumber of pages: {num_pages}\n\n')
    for page in pdf.pages:
        txt_file.writelines(page.extractText())
