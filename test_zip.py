from zipfile import ZipFile
zip_ = ZipFile('archive.zip')
print(zip_.namelist()) #список архива
text = zip_.read('example2.txt') #содержимое файла
print(text)
zip_.close()

with ZipFile('archive.zip') as myzip: #распаковка файла, для примера его сначала удалили, он появился по отработке
    myzip.extract('example2.txt')


