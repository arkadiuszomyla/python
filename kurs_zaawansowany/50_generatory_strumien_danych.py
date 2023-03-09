file = open(r'C:\Users\arkadiuszo\PycharmProjects\python_nauka\kurs_zaawansowany\data.txt')

#tak nie robić
data = file.read()
file.close()

for line in data.splitlines():
    if line.startswith('ACTION'):
        print(line)


#bardziej poprawnie, nie czyta całego pliku do pamięci
file = open(r'C:\Users\arkadiuszo\PycharmProjects\python_nauka\kurs_zaawansowany\data.txt')

for line in file:
    if line.startswith('ACTION'):
        print(line.replace('\n', ''))

file.close()


# wszystkie dane znowu wczytane do pamięci
file = open(r'C:\Users\arkadiuszo\PycharmProjects\python_nauka\kurs_zaawansowany\data.txt')

records = []

for line in file:
    if ':' in line:
        type, action = line.rstrip('\n').split(':', 1) # rstrip - Remove any white spaces at the end of the string:
        record = [type, action]
        records.append(record)

print(records)
file.close()


# nasz generator
def get_records(filePath):
    print('---opening file---')
    file = open(filePath)

    for line in file:
        if ':' in line:
            type, action = line.rstrip('\n').split(':', 1)
            record = [type, action]
            yield record

    print('---closing file---')
    file.close()


filePath = open(r'C:\Users\arkadiuszo\PycharmProjects\python_nauka\kurs_zaawansowany\data.txt')

for record in get_records(filePath):
    print('The type is {} and the action is {}'.format(record[0], [record[1]]))
