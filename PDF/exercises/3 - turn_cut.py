from pathlib import Path
from PyPDF2 import PdfFileReader,PdfFileWriter
import copy

import_path = Path.cwd()/'exercises_dir'/'split_and_rotate.pdf'
file_read_0 = PdfFileReader(str(import_path))
export_path_0 = Path.cwd() / 'exercises_dir' / 'split_and_rotate_TURNED.pdf'
export_path_1 = Path.cwd() / 'exercises_dir' / 'split_and_rotate_CUTED.pdf'
file_write_0 = PdfFileWriter()
file_write_1 = PdfFileWriter()

for page in range(file_read_0.getNumPages()):
    page_cache = file_read_0.getPage(page)
    page_cache.rotateCounterClockwise(90)
    file_write_0.addPage(page_cache)

with export_path_0.open(mode='wb') as file:
    file_write_0.write(file)

file_read_1 = PdfFileReader(str(export_path_0))

for page_num in range(file_read_1.getNumPages()):
    left_side = copy.deepcopy(file_read_1.getPage(page_num))
    right_side = copy.deepcopy(file_read_1.getPage(page_num))
    curent_coords = left_side.mediaBox.lowerRight
    print(curent_coords)
    new_coords = int(curent_coords[0]/2),curent_coords[1]
    print(new_coords)
    left_side.mediaBox.lowerRight = new_coords
    file_write_1.addPage(left_side)
    right_side.mediaBox.lowerLeft = new_coords
    file_write_1.addPage(right_side)
with export_path_1.open(mode='wb') as file:
    file_write_1.write(file)