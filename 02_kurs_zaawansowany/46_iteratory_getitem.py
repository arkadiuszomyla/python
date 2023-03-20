import datetime as dt

class MillionDays:

    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year,month,day)
        self.maxdays = maxdays

    # Metoda __getitem__(self, key)definiuje zachowanie podczas uzyskiwania dostępu do elementu przy użyciu notacji self[key].
    # Jest to również częścią protokołów kontenerów mutable i niezmiennych.
    # pozwala odwoływać się do elementów, ale jednocześnie sama w sobie nie ma iteratora
    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()

md = MillionDays(2000,1,1,2500000)

print(md[0],md[2],md[10])

#print(next(md))   #nie uruchomi się bez metody __next__

# iter pozwala iterować po obiekcie
it = iter(md)
print(next(it))
print(next(it))

for d in md:
    pass