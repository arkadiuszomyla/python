import random

myNumbers = []

while len(myNumbers) < 7:
    newNumber = random.randint(1, 49)
    if newNumber in myNumbers:
        print("Eliminated:", newNumber)
        continue
    myNumbers.append(newNumber)

print("Those numers will win:", myNumbers)