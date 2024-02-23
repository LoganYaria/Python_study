from pathlib import Path
from PyPDF2 import PdfFileReader,PdfFileWriter
import copy

pdf_read_path = Path.cwd()/'files'/'half_and_half.pdf'
pdf_write_path = Path.cwd()/'files'/'cuted_page.pdf'
pdf_read_file = PdfFileReader(str(pdf_read_path))
pdf_write_file = PdfFileWriter()
# # Пример на одной странице
page_0 = pdf_read_file.getPage(0)
print(page_0)
#print(page_0.mediaBox)
print(page_0['/MediaBox']) # информация по диагонали страницы
print(page_0.mediaBox.lowerLeft) # координаты нижнего левого угла(x,y)
print(page_0.mediaBox.lowerRight) # координаты нижнего правого угла(x,y)
print(page_0.mediaBox.upperLeft) # координаты верхнего левого угла(x,y)
print(page_0.mediaBox.upperRight) # координаты верхнего правого угла(x,y)

print(page_0.mediaBox.lowerRight[0]) # вывод нижней правой координаты x
print(page_0.mediaBox.upperRight[1]) # вывод верхней правой координы y

page_0.mediaBox.upperLeft = (0,480) #применяем новые координаты на верхний левый угол, правый верхний подтянется
# # чтобы соблюдать прямоугольный  формат страницы
print(page_0.mediaBox.upperRight)
pdf_write_file.addPage(page_0)

with pdf_write_path.open(mode='wb') as file:
    pdf_write_file.write(file)

# # Оптимальная версия
left_side = copy.deepcopy(pdf_read_file.getPage(0)) # делаем копию  странички, чтобы после проведения махинаций, не было
# # Ппроблем
right_side = copy.deepcopy(pdf_read_file.getPage(0)) # делаем еще одну копию

current_coords = left_side.mediaBox.upperRight #
new_coords = current_coords[0]/2,current_coords[1] #
left_side.mediaBox.upperRight = new_coords #
right_side.mediaBox.upperLeft = new_coords #
pdf_write_file.addPage(left_side)
pdf_write_file.addPage(right_side)

with pdf_write_path.open(mode='wb') as file:
    pdf_write_file.write(file)

# # Каличная версия обрезки
first_page = pdf_read_file.getPage(0)
left_side = copy.deepcopy(first_page)
right_side = copy.deepcopy(first_page)

left_side.mediaBox.lowerRight = (396,0)
right_side.mediaBox.lowerLeft = (396,0)

pdf_write_file.addPage(left_side)
pdf_write_file.addPage(right_side)

with pdf_write_path.open(mode='wb') as file:
     pdf_write_file.write(file)

# #Полное разделение всей книги
for page in range(pdf_read_file.getNumPages()):
    left_side = copy.deepcopy(pdf_read_file.getPage(page))
    right_side = copy.deepcopy(pdf_read_file.getPage(page))
    current_coords = left_side.mediaBox.upperRight
    new_coords = current_coords[0]/2,current_coords[1]
    left_side.mediaBox.upperRight = new_coords
    right_side.mediaBox.upperLeft = new_coords
    pdf_write_file.addPage(left_side)
    pdf_write_file.addPage(right_side)

with pdf_write_path.open(mode='wb') as file:
    pdf_write_file.write(file)
