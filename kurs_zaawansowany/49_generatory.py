# Generatory są iteratorami, rodzajem iteracji, którą można iterować tylko raz . Generatory nie przechowują wszystkich wartości w pamięci, generują je w locie
# generator to funkcja, lazy, oszczędność zasobów

import datetime as dt

def MillionDays(year, month, day, maxdays):
    date = dt.date(year, month, day)

    for i in range(maxdays):
        #yield ma za zadanie zwrócić wartość i zamrozić funkcję - zapamiętuje wartość do następnego wywołania funkcji
        '''W przypadku yield funkcji, gdy jej kod zaczyna działać (tj. po wywołaniu funkcji, zwróceniu obiektu generatora, którego next()metoda jest następnie wywoływana), podobnie umieszcza swoje zmienne lokalne na stosie i przez chwilę wykonuje obliczenia. Ale potem, kiedy trafi na yieldinstrukcję, przed wyczyszczeniem swojej części stosu i powrotem, robi migawkę swoich zmiennych lokalnych i przechowuje je w obiekcie generatora. Zapisuje również w swoim kodzie miejsce, w którym aktualnie się znajduje (tj. konkretna yieldinstrukcja).
            Jest to więc rodzaj zamrożonej funkcji, na której zawieszony jest generator.
            Kiedy next()jest wywoływana później, pobiera elementy funkcji na stos i ponownie je animuje. Funkcja kontynuuje obliczenia od miejsca, w którym została przerwana, nieświadoma faktu, że właśnie spędziła wieczność w chłodni.'''
        yield(date + dt.timedelta(days=1))


for d in MillionDays(2000, 1, 3, 3):
    print(d)


def GetMagicNumbers():
    yield(22)
    yield(4)
    yield(5)

r = GetMagicNumbers()
print(next(r))
print(next(r))
print(next(r))
print(next(r)) # stopiteration()

for m in r:
    print(m)