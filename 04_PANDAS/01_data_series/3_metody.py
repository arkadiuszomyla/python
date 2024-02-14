# metody mają dostęp do danego obiektu i mogą go modyfikować

import pandas as pd
import numpy as np
import math as math

monotonicList = (1,2,4,67,99)
monotonicSeries = pd.Series(monotonicList)
print(monotonicSeries)


print(monotonicSeries.sum()) #suma obiektów
print(monotonicSeries.min())
print(monotonicSeries.max())
print(monotonicSeries.mean()) #średnia
print(monotonicSeries.count()) #ile elementów
print(monotonicSeries.product()) #mnoży przez siebie wszystkie elementy
print(monotonicSeries.keys()) #jak został zbudowany indeks RangeIndex(start=0, stop=4, step=1)


print(monotonicSeries.to_list()) # TO_EXCEL, TO_CSV, ITD ITP

print(monotonicSeries.add(10)) #do każdego elementu dodaje 10
print(monotonicSeries) #po uruchomieniu add i następnym wywołaniu dataderies posiada wartości pierwotne,
                       # metoda add(10) tworzy tak naprawdę kopie dataseries
newSeries = monotonicSeries.add(10) #to dopiero zapisze zmodyfikowany wynik

currecies = ['USD','EUR','PLN','EUR','EUR']
countries = ['USA', 'SPAIN', 'POLAND', 'PORTUGAL', 'ITALY']

curSeries = pd.Series(countries, currecies) #lista wartości + lista indeksów
print(curSeries)

curSeries = pd.Series(data=countries, index=currecies) #lista wartości + lista indeksów
print(curSeries)

##### Obiekt serii może zawierać zduplikowane indeksy, słownik nie może zawierać zduplikowanych indeksów, w przypadku zduplikowania jest zapisywany tylko ostatni