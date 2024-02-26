import pandas as pd

index = ['a', 'b', 'c', 'd', 'e1', 'e2']
values = ['Austria', 'Belgium', 'Canada', 'Denmark', 'England', 'Estonia']
s = pd.Series(values, index)

print(s)

searchList = ['a', 'b']
print(s.loc[searchList])

searchListNotFound = ['a', 'b', 'f']
#print(s.loc[searchListNotFound]) # znajduje a i b i raise KeyError(f"{not_found} not in index")

print(s.reindex(searchListNotFound)) #zwraca nową serie, tam gdzie nie znajduje wartości zwraca - f   #     # NaN

print(s.index.intersection(searchListNotFound)) #Index(['a', 'b'], dtype='object') - a, b jako część wspólna

print(s.loc[s.index.intersection(searchListNotFound)]) #zwróci tylko a i b

index = ['a', 'b', 'c', 'd', 'e', 'e']
values = ['Austria', 'Belgium', 'Canada', 'Denmark', 'England', 'Estonia']
s = pd.Series(values, index)


#REINDEX NIE DZIAŁA DLA POWTÓRZONEGO INDEKSU
#INTERSECTiON WYŚWIETLI POPRAWNIE WARTOŚCI DLA ZDUPLIKOWANEGO INDEKSU