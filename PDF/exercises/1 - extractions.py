from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = Path.cwd() / 'zen.pdf'
pdf_file = PdfFileReader(str(pdf_path))
print(pdf_file.getNumPages())
first_page = pdf_file.getPage(0)
print(first_page.extractText())