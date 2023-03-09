import datetime as dt


class MillionDaysIterator:
    def __init__(self, date, max):
        self.date = date
        self.max = max

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret

    # nie musi być iterable, ta klasa jest iteratorem
    #def __iter__(self):
    #    return self


class MillionDays:
    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays
        self.iterator = MillionDaysIterator(self.date, self.maxdays)

    # Funkcja __iter__() zwraca obiekt iteratora, który przechodzi przez każdy element danego obiektu . Dostęp do następnego elementu można uzyskać za pomocą funkcji __next__().
    def __iter__(self):
        return self.iterator


md = MillionDays(2000, 1, 1, 2500000)

for d in md:
    print(d)
