import itertools as it

filepath = r'C:\Users\arkadiuszo\PycharmProjects\python_nauka\kurs_zaawansowany\data.txt'

data = []

with open(filepath) as file:
    for line in file:
        elements = line.rstrip("\n").split(':')
        d = {'type': elements[0], 'action': elements[1]}
        data.append(d)

print(data)

it.groupby(data, key=lambda x: x['type'])

data = sorted(data, key=lambda x: x['type'])

for key, elements in it.groupby(data, key=lambda x: x['type']):
    #print('The key is {} and the group is {}'.format(key, list(elements)))
    print('The key is {} and number of elements is {}'.format(key, len(list(elements))))
