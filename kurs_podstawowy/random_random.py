import random

print("One random numer:", random.randint(1, 100))  # od 1 do 100, bez 0
print("Choosing random number from a range", random.choice(range(1, 100)))
print("Choosing random number from a range - easier"), random.randrange(1, 100)

list = ['John', 'Ann', 'Peter', 'Susan', 'Emily', 'Greg']
random.shuffle(list)

print("Just a random float", random.random())

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
]

random.shuffle(countries)

groupNumber = 0

for i in range(len(countries)):  # W dużym uproszczeniu range generuję listę liczb, po których możemy iterować
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])

# GENEROWANIE HASEŁ
# for i in range(32, 127):    #TABELA ASCII, 32 to spacja, The chr() method converts an integer to its unicode character and returns it.
#    print(i, chr(i))


ints = range(33, 127)
password = ''
for i in range(16):
    password += chr(random.choice(ints))

print("Password is:", password)
