import os.path

from PyPDF2 import PdfReader
#docs_pdf_path=os.path.abspath(__file__) + 'resources' + 'docs-pytest-org-en-latest.pdf'

pdf_reader = PdfReader('./resources/docs-pytest-org-en-latest.pdf')
number_of_pages = len(pdf_reader.pages)
print(number_of_pages)
assert number_of_pages == 412

#печать страницы
page = pdf_reader.pages[2]
text = page.extractText()
print(text)
assert '5 Further' in text
