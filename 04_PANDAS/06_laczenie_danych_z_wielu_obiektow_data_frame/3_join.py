import pandas as pd
import os

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)      #chce widzieć wszystkie kolumny, pycharm domyślnie je ucina

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

prod_1 = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "products.csv"), usecols=['ProductID', 'ProductName'], index_col='ProductID')
prod_2 = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "products.csv"), usecols=['ProductID', 'UnitPrice', 'UnitsInStock'], index_col='ProductID')

print(prod_1.head())
print(prod_2.head())

prod_1.join(prod_2) #zwraca dataframe, indeks to ProductID, łączy dwie tabele, join pracuje tylko na indeksach
#w parametrcie ', how=left' można ustawić rigth i left - jak w sqlu


##################### dwa inne zbiory danych
categories = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "categories1.csv"), usecols=['CategoryID', 'CategoryName', 'Description'])
products = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "products.csv"), usecols=['ProductID', 'UnitPrice', 'ProductName','CategoryID'])

categories.set_index('CategoryID', inplace=True) #najpierw musimy ustawić indeks, w products nie ustawiamy
products.join(other=categories)   #to zadziałała, ale bez sensu, bo w Product jest indeks 'stworzony automatem'
products.join(other=categories, on='CategoryID') #on - określamy po czym ma łączyć