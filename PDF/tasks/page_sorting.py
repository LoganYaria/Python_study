from pathlib import Path
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger

import_path = Path.cwd()/'file_dir/scrambled.pdf'
export_path = Path.cwd()/'file_dir/correct_scrambled.pdf'
temporary_path = Path.cwd()/'file_dir/temporary_page.pdf'
read_file = PdfFileReader(str(import_path))
merge_file = PdfFileMerger()
write_file = PdfFileWriter()

for page_num in range(read_file.getNumPages()):
    transform_page = read_file.getPage(page_num)
    turning_angle = str(transform_page['/Rotate'])
    if turning_angle[0] =='-':
        transform_page.rotateClockwise(int(turning_angle[1:]))
    else:
        transform_page.rotateCounterClockwise(int(turning_angle))

    string_real_num_page =transform_page.extractText()
    if string_real_num_page[-1] == '!':
        real_num_page = (int(string_real_num_page[:-1]) - 1)
    else:
        real_num_page = (int(string_real_num_page) - 1)

    write_file.addPage(transform_page)
    with temporary_path.open(mode='wb') as file:
        write_file.write(file)
        file.close()

    merge_file.merge(real_num_page, str(temporary_path))
    with export_path.open(mode='wb') as file:
        merge_file.write(file)
        file.close()
    # temporary_path.unlink()