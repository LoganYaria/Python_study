from pathlib import Path
from PyPDF2 import PdfFileReader,PdfFileWriter

class PdfFileSplitter:
    writer1 = ''
    writer2 = ''
    def __init__(self, file_name):
        self.file_name = file_name


    def split(self, breakpoint):
        pdf_file_path = Path.cwd()/self.file_name
        pdf_file = PdfFileReader(str(pdf_file_path))
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()
        for page in pdf_file.pages[:breakpoint]:
            self.writer1.addPage(page)
        for page in pdf_file.pages[breakpoint:]:
            self.writer2.addPage(page)
        return self.writer1, self.writer1

    def write(self):
        file_write_name = input('Enter the name of file: ')
        write_path1 = Path.cwd()/str(file_write_name + '_1.pdf')
        write_path2 = Path.cwd() /str(file_write_name + '_2.pdf')
        with write_path1.open(mode='wb') as file:
            self.writer1.write(file)
        with write_path2.open(mode='wb') as file:
            self.writer2.write(file)
        return write_path1, write_path2



