from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_extraction_path = Path.cwd()/'Pride_and_Prejudice.pdf'
pdf_inscription_path = Path.cwd()/'New_PDF_2.pdf'

pdf_extraction_file = PdfFileReader(str(pdf_extraction_path))
pdf_inscription_file = PdfFileWriter()

# #Цикл фор
for number in range(1,4):
    page = pdf_extraction_file.getPage(number)
    pdf_inscription_file.addPage(page)
# #Перебор срезом
for page in pdf_extraction_file.pages[1:4]:
    pdf_inscription_file.addPage(page)

with pdf_inscription_path.open(mode='wb') as file:
    pdf_inscription_file.write(file)

# #Извлечение всех страниц из документа: метод appendPagesFromReader()
pdf_inscription_file.appendPagesFromReader(pdf_extraction_file)
with pdf_inscription_path.open(mode='wb') as file:
    pdf_inscription_file.write(file)