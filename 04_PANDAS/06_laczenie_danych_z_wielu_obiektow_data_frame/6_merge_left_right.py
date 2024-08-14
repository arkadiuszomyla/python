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

#chcemy produkty, które nie zostały jeszcze zamówione
merged = products.merge(right=orderedProducts, on='ProductID', how='left', indicator=True)
filter = merged['_merge'] == 'left_only'
print(merged[filter])

#inaczej
merged = orderedProducts.merge(right=products, on='ProductID', how='right', indicator=True)   #zamieniamy kolejność framów
filter = merged['_merge'] == 'right_only'
print(merged[filter])