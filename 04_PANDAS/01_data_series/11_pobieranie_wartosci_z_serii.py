import pandas as pd

index = ['a', 'b', 'c', 'd', 'e', 'e']
values = ['Austria', 'Belgium', 'Canada', 'Denmark', 'England', 'Estonia']
s = pd.Series(values, index)

print(s)


print(s[0])  #działa
print(s['b']) #działa
print(s['e']) #oba wyniki #seria
#print(s['f']) #KeyError: 'f'

print(s.get(0)) #działa
print(s.get('b')) #działa
print(s.get('e')) #oba wyniki #seria
print(s.get('f'))  #None

#print(s.at[0]) #TypeError: '<' not supported between instances of 'str' and 'int'
print(s.at['b']) #działa
print(s.at['e']) #oba wyniki #tablica
#print(s.at['f'])  #KeyError: 'f'

print(s.iat[0])  #działa
#print(s.iat['b']) #ValueError: iAt based indexing can only have integer indexers
#print(s.iat['e']) #ValueError: iAt based indexing can only have integer indexers
#print(s.iat['f']) #ValueError: iAt based indexing can only have integer indexers

#print(s.loc[0])  #TypeError: '<' not supported between instances of 'str' and 'int'
print(s.loc['b']) #działa
print(s.loc['e']) #oba wyniki #seria
#print(s.loc['f']) #KeyError: 'f'

print(s.iloc[0])  #działa
#print(s.iloc['b']) #TypeError: Cannot index by location index with a non-integer key
#print(s.iloc['e']) #TypeError: Cannot index by location index with a non-integer key
#print(s.iloc['f']) TypeError: Cannot index by location index with a non-integer key
