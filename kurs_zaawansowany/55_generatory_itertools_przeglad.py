import itertools
import operator

data = [1, 2, 3, 4, 5]

# accumulate - na poszczególnych kolejnych elementach wykonaj mnożenie (mul - mnożenie)
result = itertools.accumulate(data, operator.mul)
for each in result:
    print(each)

# accumulate - wyświetl największą wartość do tej pory znalezioną
data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, max)
for each in result:
    print(each)

# count - generuje kolejne wartośći, od czego zacząć i o ile powiększać
for i in itertools.count(10, 3):
    print(i)
    if i > 20:
        break

# cycle - przechodzi przez zbiór danych i robi to w nieskończoność
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
for m in itertools.cycle(months):
    print(m)


# chain - łączy dwa lub więcej obiekty iterable
color_basic = ['red', 'blue', 'yellow']
color_mix = ['green', 'orange', 'violet']
result = itertools.chain(color_basic, color_mix)
for each in result:
    print(each)

# compress - przyjmuje obiekt z danymi/TrueFalse, zwraca tylko True
cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
selections = [True, False, True, False]
result = itertools.compress(cars, selections)
for each in result:
    print(each)

# dropwhile - usuń wszystko dopóki nie zostanie spełniony warunek, potem pobierz resztę wartości
data = [1,2,3,4,5,6,7,8,10,1]
result = itertools.dropwhile(lambda x: x<5, data)
for each in result:
    print(each)

# filterfalse - opuszcza elementy które warunku nie spełniają
data = [1,2,3,4,5,6,7,8,10,1]
result = itertools.filterfalse(lambda x: x<5, data)
for each in result:
    print(each)

# islice - substring (python liczy od 0)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
result = itertools.islice(months, 6 ,8)
for each in result:
    print(each)

# product - iloczyn kartezjański, każde elementy z jednego zbioru łączy każdy element z drugiego zbioru
spades = ['Hearts', 'Tiles', 'Clovers', 'Pikes']
figures = ['Ace', 'King', 'Jack', '10']
result = itertools.product(spades, figures)
for each in result:
    print(each)

# repeat - w nieskonczoność powtarza to samo, chyba że w drugim argumencie określi się warunek
for i in itertools.repeat('tell me more', 5):
    print(i)

# starmap - dodaje po dwa elementy # zwróci 3, 7, 11
data = [{1,2}, {3,4}, {5,6}]
result = itertools.starmap(operator.add, data)
for each in result:
    print(each)

# takewhile - pobiera elementy tak długo jak warunek jest prawdziwy, resztę pomija
data = [1,2,3,4,5,6,7,8,10,1]
result = itertools.takewhile(lambda x: x<5, data)
for each in result:
    print(each)

# tee - tworzy dwa niezależne iteratory i pozwala przez nie przejść
cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
cars1, cars2 = itertools.tee(cars)
for each in cars1:
    print(each)
print('-----')
for each in cars2:
    print(each)

# zip_longest - łączy dwie listy, ale nie muszą być tej samej długości, dla pozostałych ustawia się wartość fillvalue
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
plan = ['busy', 'busy', 'busy', 'free']
result = itertools.zip_longest(months, plan, fillvalue='unknown')
for each in result:
    print(each)