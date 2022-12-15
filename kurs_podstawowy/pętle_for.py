persons = ["Aro", "Daro", "Maro", "Karo", "Sławo"]
domain = "mycompany.com"

for person in persons:
    print(person + "@" + domain)
else:
    print("Nie ma już nikogo")

##########################################################################

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for data_unit in data:
    print(data_unit.upper())

for data_unit in data:
    elements = data_unit.split(":")
    print(elements[0].upper())
    print(elements[1])

##########################################################################

for number in range(1, 21):  # można do trzech parametrów, od, do, o ile
    if number % 2 == 0:
        print(number, "jest podzielne przez 2")
        print("Number %2d is %s" % (number, "even"))
    else:
        print(number, "nie jest podzielne przez 0")
        print("Number %2d is %s" % (number, "odd"))

############################################################################

for x in range(1, 6):
    for y in range(1, 6):
        print("x = %d, y = %d, x * y = %d" % (x, y, x * y))

###########################################################################

for x in range(1, 6):
    line = str(x)
    for y in range(1, 6):
        line += '\t%3d' % (x * y)
        print(line)

###########################################################################

for candidate in range(2, 31):  # szukanie liczb pierwszych
    for divider in range(2, candidate):
        if candidate % divider == 0:
            print("%2d is not a prime number- divider is %2d" % (candidate, divider))
            break  # jeżeli jest podzielna przez cokolwiek nie ma sensu szukać dalej, zatrzymujemy wewnętrzą pętle

##########################################################################

for candidate in range(2, 31):  # szukanie liczb pierwszych
    isPrime = True
    for divider in range(2, candidate):
        if candidate % divider == 0:
            isPrime = False
            print("%2d is not a prime number- divider is %2d" % (candidate, divider))
            break  # jeżeli jest podzielna przez cokolwiek nie ma sensu szukać dalej, zatrzymujemy wewnętrzą pętle

    if isPrime:
        print("%2d is prime!" % candidate)

#########################################################################

for candidate in range(2, 31):  # szukanie liczb pierwszych
    for divider in range(2, candidate):
        if candidate % divider == 0:
            print("%2d is not a prime number- divider is %2d" % (candidate, divider))
            break  # jeżeli jest podzielna przez cokolwiek nie ma sensu szukać dalej, zatrzymujemy wewnętrzą pętle
    else:  # else dla pętli for
        print("%2d is prime!" % candidate)

#######################################################################

persons = ['Elizabeth', 'Steven@sales.mycompany.com', 'Sebastian', 'Margaret', 'Svetlana@mycompany.eu', 'Raphael']
domain = 'mycompany.com'
emails = []

for person in persons:
    if '@' in person:
        emails.append(person)
    else:
        email = person + '@' + domain
        emails.append(email)

for email in emails:
    print(email)

########################################################################

persons = ['Elizabeth', 'Steven@sales.mycompany.com', 'Sebastian', 'Margaret', 'Svetlana@mycompany.eu', 'Raphael']
domain = 'mycompany.com'
emails = []

for person in persons:
    if '@' in person:
        emails.append(person)
        continue
        email = person + '@' + domain
        emails.append(email)

for email in emails:
    print(email)
