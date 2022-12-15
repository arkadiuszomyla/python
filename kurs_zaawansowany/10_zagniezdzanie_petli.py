listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []

for a in listA:               #wyświetlanie tupletów każdy z każdym
    for b in listB:
        product.append((a,b))
print(product)

product = [(a,b) for a in listA for b in listB]  #robi to samo w jednej linii
print(product)

product = [(a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]  # % - dzieli, po podzieleniu przez 2 zwaracaja 1 lub 0, parzyste lub nieparzyste
print(product)


product = {a:b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}  # zmieniamy na słownik
print(product)