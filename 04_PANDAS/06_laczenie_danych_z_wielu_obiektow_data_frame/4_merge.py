import pandas as pd
import os

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)      #chce widzieć wszystkie kolumny, pycharm domyślnie je ucina

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

cat1 = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "categories_del_1.csv"), usecols=['CategoryID', 'CategoryName'])
cat2 = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "categories_del_2.csv"), usecols=['CategoryID', 'CategoryName'])

print(cat1,'\n', cat2) #categoryId nie zawsze się pokrywa

cat1.merge(cat2) #część wspólna dwóch zbiorów
cat1.merge(cat2, on='CategoryID') #część wspólna, otrzymujemy tu zamiast CategoryName kolumny CategorName_x i CategoryName_y
cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'])    #określamy sufiksy dodawane (zamiast domyślnie _x i _y
cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='outer')  #how - DOMYSLNIE JEST INNER, przy outer dostaniemy sume wszystkiego
cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='outer', indicator=True) #indicator dodaje dodatkową kolumnę _merge, która informuje o tym skąd wziął się dany wierszy (both, left, right)

cat_merged = cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='outer', indicator=True) #zapisujemy wynik do nowej zmiennej
cat_merged['_merge'] == 'left_only' #tylko te wiersze, które występowały tylko po lewej stronie, zwróci True/False
filter = cat_merged['_merge'] == 'left_only'
cat_merged[filter] #wyświetli tabele gdzie _merge = True