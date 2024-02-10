from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

export_path = Path()/'C:/Users/Drrragonborn/PycharmProjects/Python_study/PDF/extraction/Pride_and_Prejudice.pdf'
import_path = Path.cwd()/'Last_page.pdf'
import_path_1 = Path.cwd()/'Even_pages.pdf'
import_path_2 = Path.cwd()/'PartI.pdf'
import_path_3 = Path.cwd()/'PartII.pdf'

export_object = PdfFileReader(str(export_path))
import_object = PdfFileWriter()

import_object.addPage(export_object.pages[-1])

with import_path.open(mode='wb') as file:
    import_object.write(file)

import_object_1 = PdfFileWriter()
num_pages = len(export_object.pages[:])
print()

for page in range(0, num_pages):
    if page % 2 == 0:
        import_object_1.addPage(export_object.getPage(page))
with import_path_1.open(mode='wb') as file:
    import_object_1.write(file)

import_object_2 = PdfFileWriter()
import_object_3 = PdfFileWriter()

for page in export_object.pages[:150]:
    import_object_2.addPage(page)
for page in export_object.pages[150:]:
    import_object_3.addPage(page)

with import_path_2.open(mode='wb') as file:
    import_object_2.write(file)
with import_path_3.open(mode='wb') as file:
    import_object_3.write(file)