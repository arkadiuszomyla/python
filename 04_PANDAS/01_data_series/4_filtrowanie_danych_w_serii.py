import pandas as pd

numbers = [1, 2, 3, 11, 12, 13]
print(numbers)
# numbers > 10 #nie działa na liście

numSeries = pd.Series(numbers)
print(numSeries)

print(numSeries > 10)  # dla każdego elemntu z serii zwraca True albo False

print(numSeries.where(numSeries > 10))
'''zwraca:
0     NaN
1     NaN
2     NaN
3    11.0
4    12.0
5    13.0
dtype: float64

jak wykluczyć NaN:
'''
print(numSeries.where(numSeries > 10, other=-1)) #dla niespełniających warunku zwróci -1
print(numSeries.where(numSeries > 10).dropna()) #wyrzuca niepasujące wyniki, numSeries nadal zawiera wszystkie elementy
print(numSeries.where(numSeries > 10, inplace=True)) #to nic nie zwróci, ale zmodyfikuje serie i wartości niespełniające warunku zamieni na NaN
numSeries.dropna(inplace=True) #nic nie zwróci, ale zmodyfikuje serie trwale usuwając elementy NaN w numSeries

'''filtrowanie po indeksie'''
print(numSeries.filter(items=[0,2,4]))