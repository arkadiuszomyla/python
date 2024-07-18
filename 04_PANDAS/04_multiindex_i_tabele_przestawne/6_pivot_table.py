import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sales = pd.read_csv(os.path.join(parent_directory, "course-files", "WA_Sales_Products_2012-14.csv"))

print(sales.head())

print(sales.pivot_table(index='Retailer country', columns=['Year', 'Quarter'], values='Revenue')) #index - co ma być w wierszach, columns - co w kolumnach, values - wartości, które mają być wyświetlane w poszczegolnych komórkach tej nowej tabeli, domyślna funkcja podczas obliczen to średnia

print(sales.pivot_table(index='Retailer country', columns='Year', values='Revenue')) #średnia sprzedaży dla kraju w skali roku

print(sales.pivot_table(index='Retailer country', columns='Year', values='Gross margin', aggfunc='min')) #minimalna marża dla kraju w skali roku

print(sales.pivot_table(index='Retailer country', columns='Year', values='Gross margin', aggfunc=['min', 'max']))  #minimalna marża dla kraju w skali roku, a zaraz obok maksymalna, czad!

pivTAb = sales.pivot_table(index='Retailer country', columns='Year', values='Gross margin', aggfunc=['min', 'max'])
print(pivTAb.columns)

print(pivTAb.swaplevel(axis='columns')) #zamienia kolejnością Year i aggfunc - poprzednia lekcja, dane nie posortowane ze względu na lata
print(pivTAb.swaplevel(axis='columns').sort_index(axis='columns'))
pivTab = pivTAb.swaplevel(axis='columns').sort_index(axis='columns') #zapisujemy