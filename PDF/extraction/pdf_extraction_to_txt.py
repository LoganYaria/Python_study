from pathlib import Path
from PyPDF2 import PdfFileReader

pdf_path = Path.cwd()/'Pride_and_Prejudice.pdf'
txt_path = Path.cwd()/'PrIdE_AnD_PrEjUdIcE.txt'
#txt_path.touch()
pdf = PdfFileReader(str(pdf_path))
with txt_path.open(mode='a',encoding='utf-8',newline='') as txt_file:
    for page in pdf.pages:
        txt_file.writelines(page.extractText())
