from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

import_path = Path.cwd()/'file_dir/newsletter.pdf'
export_path = Path.cwd()/'file_dir/enc_newsletter.pdf'

file_read = PdfFileReader(str(import_path))
file_write = PdfFileWriter()

file_write.appendPagesFromReader(file_read)
# # file_write.encrypt(user_pwd='SuperHOT') пароль пользователя = пароль хозяина
file_write.encrypt(user_pwd='SuperHOT', owner_pwd='SuperDuperHOT')
with export_path.open(mode='wb') as file:
    file_write.write(file)