from pdf_file_splitter import PdfFileSplitter

pdf_file = PdfFileSplitter('Pride_and_Prejudice.pdf')
pdf_file.split(1)
pdf_file.write()