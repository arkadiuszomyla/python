import pandas as pd
import os

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)      #chce widzieć wszystkie kolumny, pycharm domyślnie je ucina

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

categories = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "categories1.csv"), usecols=['CategoryID','CategoryName','Description'])
products = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "products.csv"), usecols=['ProductID','ProductName','CategoryID','UnitPrice'])

products.merge(right=categories, on='CategoryID') #część wspólna

categories.rename({'CategoryID': 'ID'}, axis='column', inplace=True) #psujemy dane, merge już nie zadziała
#możemy wrócić do starej nazwy kolumny albo:
products.merge(right=categories, left_on='CategoryID', right_on='ID') #left_on, right_on - możemy sami wybrać kolumny, po których się łączyć


# parametr suffixes=['',''] - sufiksy jeżeli kolumny mają takie same nazwy
# parametr sort=True - automatyczne sortowanie przy merge-u
# parametr right_index=True - automatyczne wyszukiwanie indeksu, łączy po indeksie dla prawej strony
# merge potrafi łączyć multiindex