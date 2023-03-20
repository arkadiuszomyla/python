import sys

print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV')
print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=';')
print('I like computers ','TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=' but better is ')
ProgramName = 'BBC'
Item = 'News'
Time = '18:00'
print('I like watching',Item,'at',Time,'on',ProgramName,'.')
print('I like watching ',Item,' at ',Time,' on ',ProgramName,'.', sep='')

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

quote.upper()
# lub
print(quote.upper())

quote.lower()
# lub
print(quote.lower())

quote.endswith('street')
# lub
print(quote.endswith('street'))

quote.isupper()
# lub
print(quote.isupper())

quote.upper().isupper()
# lub
print(quote.upper().isupper())

quote.find('one')
# lub
print(quote.find('one'))

quote.replace('one', '1')
# lub
print(quote.replace('one', '1'))

quote.replace('one', '1').replace('both', '2')
# lub
print(quote.replace('one', '1').replace('both', '2'))

quote.split(' ')
# lub
print(quote.split(' '))

quote.isdigit()
quote.isdecimal()
quote.isalpha()
quote.isalnum()
# lub
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())

firstName = 'Kasia'
familyName = 'Sowa'
lastName = 'Mrugala'

newName = firstName+familyName+lastName
print(newName)

newName = firstName+" "+familyName+" "+lastName
print(newName)

music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'
# or
music = "\"Universal Fanfare\" Jerry Goldsmith \"Happy Together\" Garry Bonner \"I'm a Man\" Steve Winwood"
print(music)

music = '"Universal Fanfare" Jerry Goldsmith\n"Happy Together" Garry Bonner\n"I\'m a Man" Steve Winwood\a'
print(music)

print('(\\(\\')
print('(-.-)')
print('O_(")(")')



#print(article.upper())
#print(article.lower().replace('monty', 'flying'))
#print(article.split(' '))
#print('word python appears', article.lower().count('python'), 'times')

print('to print the \\ you need to put \\ twice in your text like this: \\\\')
print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")
amountPLN = 234
print('cur', '\texchange', 'amount')
print('USD', "\t", 3.65, "\t", amountPLN / 3.65)
print('EUR', '\t', 4.23, "\t", amountPLN / 4.23)
valueAsText = '123.45'
factor = 1.23
print('value is ', valueAsText, 'factor is', factor, 'value*factor=', float(valueAsText) * factor)

helloMessage = "Hello %s!"

print(helloMessage % ("Kate"))
print(helloMessage % ("Chris"))

helloMessage = "Hello {0:s}!"

print(helloMessage.format("Kate"))
print(helloMessage.format("Chris"))

helloMessage = "%s has %d %s"

print(helloMessage % ("Kate", 1, "animal"))
print(helloMessage % ("Chris", 100000, "$"))

helloMessage = "{0:s} has {1:d} {2:s}"

print(helloMessage.format("Kate", 1, "animal"))
print(helloMessage.format("Chris", 100000, "$"))

line = "{0:20s} costs {1:6d} €"

print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))

line = '{0:s} {1:d}'

print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))

number = '100'
print(int(number) + 1)
print(type(number))

message1 = 'processing file %s'
disk = 'C:\\'
folder = 'FOLDER\\'
file = 'FILE'

print(message1 % ('file_1.txt'))
print(message1 % (disk + folder + file))

message2 = 'File %s has size %d KB'
print(message2 % (disk + folder + file, 100))

message3 = 'File %20s has size %10d KB'  # ilosc znaków zarezerwowanych na napis lub liczbę
message4 = 'Processing file {0:s}'
print(message4.format(disk + folder + file))

message5 = 'Processing file {0:s} has size {1:d}'  # parametry liczone od 0
print(message5.format(file, 100))

#print(sys.maxsize)
five = 5
three = 3
print(five + three)
print(five / three)
print(five // three)  # zwraca liczbę całkowitą
print(five % three)  # modulo -reszta z dzielenia

iSWeekeend = True
print('Is weekend =', iSWeekeend)
temperature = 22
print('Temperature = ', temperature)
isHappy = iSWeekeend and temperature >= 20
print('Czy jestem Happy', isHappy)
isHappy = not iSWeekeend and temperature >= 20

a = 1
b = 1
c = 1

a = b = c = 2
c = 3

a ** 3 ** 2  # a do trzeciej do drugiej
x = 1
x = x + 1
x += 1
print(x)
x += 2
print(x)
x -= 1

# String jako tablica znaków
string = 'Tablica znaków'
print(string[0])  # T
print(string[2:5])  # substring
print(string[:8])  # wszystkie znaki do ósmego, i można od ósmego

message = 'Document "cv.doc" was printed on printer: XEROX '
print(message.find(':'))
print(message[message.find(':'):])
print(message[message.find(':') + 2:])

# print(message[message.find('"') + 1:])
# tmp = message[message.find('"') + 1:]
# print(tmp[:tmp.find('"')])
