import pandas as pd
import os

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)      #chce widzieć wszystkie kolumny, pycharm domyślnie je ucina

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

categories = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "categories1.csv"))
products = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "products.csv"))
suppliers = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "suppliers.csv"))
customers = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "customers.csv"))

print(categories.head())
print(products.head())
print(suppliers.head())
print(customers.head())