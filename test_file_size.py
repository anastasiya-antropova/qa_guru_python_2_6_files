import os.path


def test_file_size():
    picture_size = os.path.getsize('./resources/sampleFile.jpeg')
    assert picture_size == 4096

    print(os.path.abspath('./resources/sampleFile.jpeg'))  # вывод абсолютного пути к файлу для переиспользования, например

os.path.dirname(os.path.abspath('./resources/sampleFile.jpeg')) #абс путь к директории

#способ склейки пути - может пригодиться для запуска с разных систем
# current_dir = os.path.dirname(os.path.abspath(__file__)) #универсальный способ поиска файла, откуда запущен код
# resources = os.path.join(current_dir, 'resources')
# print(resources)
# resources_tmp = os.path.join(current_dir, 'resources', 'tmp') #даже несущ-е папки
# print(resources_tmp)
