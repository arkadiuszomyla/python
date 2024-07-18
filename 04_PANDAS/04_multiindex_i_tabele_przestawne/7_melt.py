import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sales = pd.read_csv(os.path.join(parent_directory, "course-files", "WA_Sales_Products_2012-14.csv"))


print(sales.pivot_table(index='Retailer country', columns='Year', values='Revenue', aggfunc='sum')) #średnia sprzedaży dla kraju w skali roku; budujemy tabele przestawną aby zaprezentować jak działa melt
pt = sales.pivot_table(index='Retailer country', columns='Year', values='Revenue', aggfunc='sum')


print(pt.index)
pt.reset_index(inplace=True) #aby było wiarygodniej dla wczytywanego pliku
pt.fillna(0, inplace=True) #zamień Na na 0, jakby nie było wartości

#melt zamienia table_pivot na obiekt data frame
#id_vars - co ma być indeksem,
#value_vars - wartości, które należy 'odpivotować'
#var_name - po 'odpivotowaniu' kolumny zostaną przeniesione do wierszy, powstanie nowa kolumna i trzeba nadać jej nazwę
#value_name - wartości zostaną przedstawione też jako dodatkowa kolumna, trzeba ją nazwać
pt.melt(id_vars='Retailer country') #nagłówki kolumn (2012,2013,2014) stają się wartościami w wierszach w kolumnie Year, wartości pojawiają się w kolumnie value
pt.melt(id_vars='Retailer country', value_name='RevenueSum') #zmienia się nazwa kolumny value
pt.melt(id_vars='Retailer country', value_name='RevenueSum', var_name='YearofTransaction') #i zmieniamy też nazwę kolumny Year

print(pt.columns) #Year było domyślni ustawione
'''
Index(['Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'China',
       'Denmark', 'Finland', 'France', 'Germany', 'Italy', 'Japan', 'Korea',
       'Mexico', 'Netherlands', 'Singapore', 'Spain', 'Sweden', 'Switzerland',
       'United Kingdom', 'United States'],
      dtype='object', name='Retailer country')
Index(['Retailer country', 2012, 2013, 2014], dtype='object', name='Year')
'''

pt.melt(id_vars='Retailer country', value_name='RevenueSum', var_name='YearofTransaction', value_vars=[2013])