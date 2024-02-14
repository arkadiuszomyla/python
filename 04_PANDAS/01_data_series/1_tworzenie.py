import pandas as pd


cities = ['London', 'Berlin', 'Warsaw', 'Paris']
print(cities)
print(pd.Series(cities))


primeNumbers = (2,3,5,7,11,13,17,19)
print(pd.Series(primeNumbers))


logicalValues = [True, True, False]
print(pd.Series(logicalValues))



spielbergFilmography = {'Jaws': 1975,
                        '1941': 1979,
                        'Indiana Jones and the Raiders of the Lost Ark': 1981,
                        'E.T.': 1982}

print(spielbergFilmography)
#indeksem staje się pierwsza określona wartość
print(pd.Series(spielbergFilmography))