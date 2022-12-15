workDays = [15,21,22,21,20,22]

print(workDays)

enumeratedDays = enumerate(workDays)
print(enumeratedDays)  #<enumerate object at 0x0000019DC11EB700>

enumeratedDays = list(enumerate(workDays))
print(enumeratedDays)  #zwraca listę zawierającą tuple pozycja-wartość [(0, 15), (1, 21), (2, 22), (3, 21), (4, 20), (5, 22)]

for pos, value in enumeratedDays:
    print('Pozycja:', pos, 'Wartość:', value)      #dobre jak chcesz uporządkować, wprowadzić indeks

months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthsDays = zip(months, workDays) #łączy dwie listy
print(monthsDays)  #<zip object at 0x0000025644207A00>

monthsDays = list(zip(months, workDays)) #łączy dwie listy
print(monthsDays)   #zwraca listę tupli po połączeniu dwóch list [('I', 15), ('II', 21), ('III', 22), ('IV', 21), ('V', 20), ('VI', 22)]

for m, d in monthsDays:
    print('Miesiąc:', m, 'Dzień:', d)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position', pos, 'month', m, 'days', d)