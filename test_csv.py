import csv
def test_csv():
    with open('resources/SampleCSVFile_11kb.csv') as csvfile:
        table = csv.reader(csvfile)
        #row_count = sum(1 for row in table) #подсчет количества строк
        #print(row_count)

        # печать столбца
        # for row in table:
        #     print(row[1])

        #поиск по строке и по индексу в строке
        for line_no, line in enumerate(table, 1):
            if line_no == 2:
                print(line)
                print(line[1])
