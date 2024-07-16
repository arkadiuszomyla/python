import pandas as pd

color = ['green', 'green', 'blue', 'blue', 'red', 'red', 'white']
size = ['S', 'S', 'S', 'M', 'M', 'M', 'L']
gender = ['M', 'W', 'M', 'W', 'M', 'W', 'U']
clothes = pd.DataFrame({'color': color, 'size': size, 'gender': gender})


clothes['color'].is_unique  #zwróci False, kolor nie jest unikalny
clothes['color'].unique()   #zwraca listę wartości, które są unikalne
clothes['color'].nunique()  #zwróci liczbę ile wartości jest unikalnych

clothes['color'].duplicated(keep='first') #zwraca True lub False dla elementów, które się powtarzają lub nie, parametr keep = first dla pierszego wystąpienia np. zielonego koloru zwróci False, dla reszty zielonych True
clothes['color'].duplicated(keep='last')  #zwraca odwrotnie niż wyżej
clothes['color'].duplicated(keep=False) #zwraca True dla wszystkich powtarzających się wartaści, jak się powtarza to jest True

uniqueValues = clothes['color'].duplicated(keep='first')
clothes[uniqueValues] #wszystkie ubrania unikalne pod względem koloru, jeżeli dwa wiersze miałyby się powtórzyć, będzie wyświetlony tylko pierwszy
clothes[~uniqueValues] #można to zanegować


clothes.drop_duplicates(subset=['color'], keep='first') #usuwa duplikaty w zależności od ustawionych parametrów

clothes.drop_duplicates(subset=['color', 'size']) #można dla wielu kolumn