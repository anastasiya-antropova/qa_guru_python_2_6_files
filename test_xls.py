import xlrd
book = xlrd.open_workbook('resources/file_example_XLS_10.xls')
print(book.nsheets) #колво страниц
print(book.sheet_names())
sheet = book.sheet_by_index(0)
print(sheet.ncols) #колво столбцов
print(sheet.nrows) #колво строк
print(sheet.cell_value(rowx=9, colx=1)) #обращение к значению строки

#печать всех строк
for rx in range(sheet.nrows):
    print(sheet.row(rx))
