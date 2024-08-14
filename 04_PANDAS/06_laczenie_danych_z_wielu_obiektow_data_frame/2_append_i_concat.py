import pandas as pd
import os

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)      #chce widzieć wszystkie kolumny, pycharm domyślnie je ucina

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

suppliers = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "suppliers.csv"), usecols = ['SupplierID', 'CompanyName', 'Country'])
customers = pd.read_csv(os.path.join(parent_directory, "course-files\\northwind-mongo-master", "customers.csv"), usecols= ['CustomerID', 'CompanyName', 'Country'])

print(suppliers.head())
print(customers.head())

len(suppliers) #29
len(customers) #91

print(suppliers.append(customers)) #łączy po wpsólnych kolumnach, nie id,
                                   #The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
                                   #120 wierszy łącznie, indeksy wzięte z tabel pierwotnych

print(suppliers.append(customers, ignore_index=True))  #tworzy jeden wspólny indeks, zamiast dwóch

supplier2 = suppliers.copy() #orginal jeszcze się przyda
supplier2.reneme({'SupplierId': 'CustomerId'}, axis='columns', inplace=True) #zmieniamy nazwę kolumny
supplier2.append(customers) #łączymy dwie tabale, 120 wierszy


################################ concat ##############################
df_concatenated = pd.concat(objs=[suppliers, customers])   #łączymy tabele przez concat, można łączyć większą ilość obiektów
len(df_concatenated) #120
print(df_concatenated.head()) #łączy po kolumnach, indeks sklejony

df_concatenated = pd.concat(objs=[suppliers, customers], ignore_index=True)   #można zrobić jeden 'spójny' indeks

df_concatenated = pd.concat(objs=[supplier2, customers], ignore_index=True)  #po zmianie nazwy kolumny