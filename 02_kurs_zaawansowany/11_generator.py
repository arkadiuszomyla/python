listA = list(range(6))
listB = list(range(6))

product = [(a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]  # % - dzieli, po podzieleniu przez 2 zwaracaja 1 lub 0, parzyste lub nieparzyste
print(product)


gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)  #generator to nie jest gotowa lista, to zapis informacji w jaki sposób generować elementy z listy
print(gen)                                                                #kiedy nie chcesz przechowywać danych w pamięci

print(next(gen))  #zwraca pierwszą wartość w generatorze
print(next(gen))  #zwroci drugą wartość

for x in gen:
    print(x)   #zwraca wszystkie wartości generatora

for x in gen:  #drugi raz nie wyświetli nic więcej, wszystko co miało zostać wygenerowane, zostało wygenerowane
     print(x)

gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
while True:   #sprawdza czy wszystko zostało wygnerowane
    try:
        print(next(gen))
    except StopIteration:
        print('all values have been generated')
        break