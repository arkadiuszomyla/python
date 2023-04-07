import random
my_number = random.randint(0,10)
start_number = -1
liczba_zgadniec = 0

while my_number != start_number:
    print("Podaj swoją liczbę")
    guess = int(input())

    if my_number == guess:
        print("GRATULACJE, CYFRA TO: ", guess, "ZGADŁEŚ ZA", liczba_zgadniec + 1, "RAZEM")
    elif my_number != guess:
        print("ZGADUJ DALEJ")

    start_number = guess
    liczba_zgadniec += 1



