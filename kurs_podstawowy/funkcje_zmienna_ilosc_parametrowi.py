
def DoAction(action, parameter):
    print("action:", action)
    print("parameter:", parameter)
    return

DoAction('buy', 'shoes')

def DoAction2(action, *parameter):
    print("action:", action)
    print("parameter:", parameter)
    return

DoAction2('buy', 'shoes', 'socks')

def DoAction3(action, what, **parameter):
    print("action:", action)
    print("what:", what)
    print("parameter:", parameter)
    return

DoAction3('buy', 'shoes', size=45, color='brown', type='sport')



'''A teraz kolej na DaysToEndOfYear:
zmień parametr tak, aby przyjmował wiele dat (uwaga funkcja będzie przyjmować daty, a nie osobne wartości rok/miesiąc/dzień)
dla każdej daty z parametrów ma zostać wyświetlona informacja o dacie i ilości dni do Sylwestra
usuń część funkcji odpowiadającą za zwracanie wartości
przetestuj działanie funkcji przekazując różną ilość argumentów '''

from datetime import date


def DaysToEndOfYear(*dates):
    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)


DaysToEndOfYear(date(1999, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15), date(2019, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15), date(2019, 1, 15), date.today())
