from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

import_path = Path.cwd()/'file_dir/enc_newsletter.pdf'
read_file = PdfFileReader(str(import_path))
export_path = Path.cwd()/'file_dir/decr_newsletter.pdf'
write_file = PdfFileWriter()
print(read_file.decrypt(password='SuperDuperHOT')) # # расшифрование pdf 0 - неверный пароль; 1 - юзер; 2 - овнер
write_file.appendPagesFromReader(read_file)

with export_path.open(mode='wb') as file:
    write_file.write(file)