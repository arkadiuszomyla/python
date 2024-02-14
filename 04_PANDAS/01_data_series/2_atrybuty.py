import pandas as pd


cities = ['London', 'Berlin', 'Warsaw', 'Paris']

citiesSeries = pd.Series(cities)

print(citiesSeries)

# atrybut jako metoda, którą posiada każdy obiekt
print(citiesSeries.size) #ilość elemenetów
print(citiesSeries.nbytes) #ile bajtów
print(citiesSeries.is_unique) #czy unikalne
print(citiesSeries.is_monotonic) #czy są posortowane
print(citiesSeries.index) #tu zwróci RangeIndex(start=0, stop=4, step=1)
print(citiesSeries.values) #['London' 'Berlin' 'Warsaw' 'Paris']
print(citiesSeries.dtype) #object
print(citiesSeries.shape) #ile elementów w ilu wymiarach
