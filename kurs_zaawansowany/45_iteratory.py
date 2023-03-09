import datetime as dt
import sys

start = dt.datetime.now()
print("Execution started at: {}".format(start))

# lista dat, w których dodajemy do dat po jednym dniu
#dates = [dt.date(2000, 1, 1) + dt.timedelta(days=i) for i in range(2500000)]
#print('size of dates is {}'.format(sys.getsizeof(dates)))
#for d in dates:
#    pass

class MillionDays:
    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    # Metoda Pythona __next__ zwraca dowolny element reprezentujący „następny” element podczas iteracji obiektu, na którym została wywołana .
    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret

    # Funkcja __iter__() zwraca obiekt iteratora, który przechodzi przez każdy element danego obiektu . Dostęp do następnego elementu można uzyskać za pomocą funkcji __next__().
    def __iter__(self):
        return self


md = MillionDays(2000, 1, 1, 2500000)
print('size of MilionDat object is: {}'.format(sys.getsizeof(md)))
for d in md:
    pass




md = MillionDays(2000, 1, 1, 2500000)

#funkcja next zwraca kolejne wartości dla iteratora
print(next(md))
print(next(md))
print(next(md))

for i in range(2500000):
    next(md)

stop = dt.datetime.now()
print("Execution stopped at: {}".format(stop))
print("Total time: {}".format(stop - start))