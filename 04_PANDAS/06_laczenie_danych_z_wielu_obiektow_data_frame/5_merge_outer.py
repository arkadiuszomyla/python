import pandas as pd
import os

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)      #chce widzieć wszystkie kolumny, pycharm domyślnie je ucina

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

products = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "products.csv"), usecols=['ProductID', 'ProductName'])
orderedProducts = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "order-details_del.csv"), usecols=['OrderID', 'ProductID','UnitPrice','Quantity'])

#chcemy wyświetlić produkty, które się nie sprzedały
merged = products.merge(right=orderedProducts, on='ProductID', how='outer', indicator=True)
filter = merged['_merge'] == 'left_only'
print(merged[filter])