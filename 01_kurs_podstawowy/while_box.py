'''  WERSJA 1, BEZ SPRAWDZANIA CZY COŚ JESZCZE WEJDZIE
cargo = [4, 40, 2, 5, 6, 20, 3, 4, 60] #wagi paczek

boxCapacity = 90 #pojemność pudła
box = [] #deklaruje zawartosc pudła
i = 0

while sum(box) + cargo[i] < boxCapacity and i < len(cargo):
    box.append(cargo[i])
    i += 1

print("The collected items sum is: ", sum(box))
print("The elements are:", box)
'''

''' WERSJA 2, NAJPIERW SORTUJE LISTE
cargo = [4, 40, 2, 5, 6, 20, 3, 4, 60] #wagi paczek
cargo.sort()

print("The cargo list is:", cargo)

boxCapacity = 90 #pojemność pudła
box = [] #deklaruje zawartosc pudła
i = 0

while sum(box) + cargo[i] < boxCapacity and i < len(cargo):
    box.append(cargo[i])
    i += 1

print("The collected items sum is: ", sum(box))
print("The elements are:", box)
'''

''' WERSJA 3, NAJPIERW WKLADAMY NAJWIEKSZE
cargo = [4, 40, 2, 5, 6, 20, 3, 4, 60] #wagi paczek
cargo.sort()
cargo.reverse()

print("The cargo list is:", cargo)

boxCapacity = 90 #pojemność pudła
box = [] #deklaruje zawartosc pudła
i = 0

while sum(box) + cargo[i] < boxCapacity and i < len(cargo):
    box.append(cargo[i])
    i += 1

print("The collected items sum is: ", sum(box))
print("The elements are:", box)
'''

cargo = [4, 40, 2, 5, 6, 20, 3, 4, 60]  # wagi paczek
cargo.sort()
cargo.reverse()

print("The cargo list is:", cargo)

boxCapacity = 90  # pojemność pudła
box = []  # deklaruje zawartosc pudła
i = 0

while i < len(cargo) and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i += 1

print("The collected items sum is: ", sum(box))
print("The elements are:", box)
