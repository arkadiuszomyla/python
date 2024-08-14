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
orders = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "order-details.csv"))

cart_prod = products.merge(categories, on='CategoryID')
cart_prod_orders = cart_prod.merge(orders, on='ProductID', suffixes=['_Prod', '_Order'])