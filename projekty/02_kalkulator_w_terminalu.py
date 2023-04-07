num = 0
operation = None
reset = True
result = None
calcOperation = ["+", "-", "*", "/", "**"]

while True:
    if reset:
        num = int(input("Podaj liczbę startową: "))
        reset = False

    operation = input("Podaj rodzaj operacji arytmetycznej" + str(calcOperation) + "lub wpisz exit jeśli koniec, reset jeśli reset: ")
    if operation == "exit":
        break

    if operation == 'reset':
        reset = True
        continue

    if operation not in calcOperation:
        print("Niedozwolona operacja")
        continue

    secondNum = int(input("Podaj drugą liczbę: "))

    if operation == "+":
        result = num + secondNum

    if operation == "-":
        result = num - secondNum

    if operation == "*":
        result = num * secondNum

    if operation == "/":
        result = num / secondNum

    if operation == "**":
        result = num ** secondNum

    print("Wynik: {}".format(str(result)))
    reset = True