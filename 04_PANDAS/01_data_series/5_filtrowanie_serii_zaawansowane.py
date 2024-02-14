import pandas as pd

numSeries = pd.Series([1, 2, 3, 11, 12, 13])


print(numSeries % 2 == 1) #True lub False dla liczb parzystych


'''jak wyświetlić liczby parzyste większe od 10 z jednej serii'''
#numSeries.where(numSeries % 2 == 1 and numSeries > 10) #nie zadziała, tworzymy dwie nowe serie dla każdego z warunków

numSeriesGreater10 = numSeries > 10
numSeriesOdd = numSeries % 2 == 1

print(numSeriesGreater10) #True False
print(numSeriesOdd) #True False

print(numSeries.where(numSeriesGreater10 & numSeriesOdd)) # & pracuje na bitach
'''
0     NaN
1     NaN
2     NaN
3    11.0
4     NaN
5    13.0
dtype: float64
'''
print(numSeries.where(numSeriesGreater10 & numSeriesOdd).dropna())
'''
3    11.0
5    13.0
dtype: float64
'''

print(numSeries.between(3,12)) #pomiędzy 3,a 12 - True False