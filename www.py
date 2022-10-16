import os
import zipfile
from PyPDF2 import PdfReader
from openpyxl import load_workbook


def test_writing_to_zip():
    z = zipfile.ZipFile('./resources/test_zip.zip', 'w')
    for folder, subfolders, files in os.walk('./resources'):
        for file in files:
            if file.endswith('.pdf') or file.endswith('.csv') or file.endswith('.xlsx'):
                z.write(os.path.join(folder, file), file)
    z.close()