import os.path
import shutil
import zipfile
from zipfile import ZipFile
from PyPDF2 import PdfReader
from openpyxl import load_workbook

folder_name ='resources_hw'
pdf_file = 'docs-pytest-org-en-latest.pdf'
xlsx_file = 'file_example_XLSX_50.xlsx'
csv_file = 'SampleCSVFile_11kb.csv'
zip_file = 'zip_hw.zip'
add_file_pdf = os.path.join(folder_name, pdf_file)
add_file_xlsx = os.path.join(folder_name, xlsx_file)
add_file_csv = os.path.join(folder_name, csv_file)

def test_create_zip():
    with zipfile.ZipFile(zip_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(add_file_pdf, arcname='pdf_add.pdf')
        zf.write(add_file_xlsx, arcname='xlsx_add.xlsx')
        zf.write(add_file_csv, arcname='csv_add.csv')
        zf.close()
    new_place = shutil.move(zip_file, 'resources_hw/')  # перемещение архива

def test_read_pdf():
    with ZipFile(os.path.join(folder_name, zip_file)) as zf:
        #with ZipFile('./resources_hw/zip_hw.zip') as zf:
        pdf_reader = PdfReader(zf.open('pdf_add.pdf'))
        assert len(pdf_reader.pages) == 412
        assert '5 Further' in pdf_reader.pages[2].extractText()

def test_read_xlsx():
    with ZipFile(os.path.join(folder_name, zip_file)) as zf:
        workbook = load_workbook(zf.open('xlsx_add.xlsx'))
        sheet = workbook.active
        assert sheet.cell(row=3, column=2).value == 'Mara'

def test_read_csv():
    with ZipFile(os.path.join(folder_name, zip_file)) as zf:
       csv_open = zf.read('csv_add.csv').decode('utf-8')
       row_count = sum(1 for row in csv_open)
       assert row_count == 10898

#def test_delete_zip():
#    os.remove('./resources_hw/zip_hw.zip')
