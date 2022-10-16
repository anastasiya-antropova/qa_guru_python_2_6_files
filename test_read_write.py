#контекстный менеджер
# with open('example.txt','w') as f: #'w' - ключ открывает файл на запись, 'r' - на чтение, 'a' -дозапись в конец, 'x' - контроль, чтобы не изменялся существ файл и не созд новый с текущ назв
#     f.write('Hello, world\nNew row')
#f.write('123') #вернется ошибка, тк файл уже закрыт

#можно и так, но это антипаттерн - надо файл закрывать вручную
# f = open('example2.txt', 'w')
# f.write('Hi')
# f.close()
# f.write('world') #вернется ошибка, потому что файл закрыт уже

# with open('example.txt') as f: #сейчас ключ r по умолчанию, не указываем
#     file = f.read()
#     print(file)
#     assert file == 'Hello, world\nNew row' #проверка файла, что есть нужный текст
#     assert 'New' in file #проверка части текста в файле
#
# def test_rows():
#     with open('example2.txt', 'r') as file: #построчная печать  ???почему через пустую строку?
#         for i in file:
#             assert i == 'Hello'
#             print(i)


with open('example3.txt', 'a') as f: #дозапись файла в конец. В середину так просто нельзя, ток костыль
    f.write('Hi\n')