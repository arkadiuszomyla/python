import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sales = pd.read_csv(os.path.join(parent_directory, "course-files", "WA_Sales_Products_2012-14.csv"))

groups = sales.groupby(by=['Retailer country'])

#chcemy wyświetlić nazwy poszczególnych krajów
for country in groups:
    print(country[0])

#można ewentualnie tak:
country_names = []
for country in groups:
    country_names.append(country[0])
print(country_names)

#chcemy wyświetlić zawartość poszczególnych grup
for country in groups:
    print(country[1])

#chcemy wyświetlić nazwę kraju i ilość wierszy, które dotyczą tego kraju
for country in groups:
    print(country[0], len(country[1]))

#można też tak:
for country, country_data in groups:
    print(country, len(country_data))

#jaka jest różnica między nawyższą traksakcją, a najniższą transakcją w danym kraju
for country, country_data in groups:
    print(country,
          country_data['Revenue'].max() - country_data['Revenue'].min())

#jaka jest maksymalna transakcją w danym kraju, i jakie to były transakcje
for country, country_data in groups:
    print(country,
          country_data['Revenue'].max(),
          country_data['Revenue'].idxmax())   #na której pozycji jest transakcja

for country, country_data in groups:
    print(country,
          country_data['Revenue'].max(),
          country_data['Revenue'].idxmax(),
          country_data.loc[country_data['Revenue'].idxmax()])

#inaczej:
the_biggest = pd.DataFrame()
for country, country_data in groups:
    the_biggest = the_biggest.append(country_data.loc[country_data['Revenue'].idxmax()])
print(the_biggest)

#albo inaczej:
sales.nlargest(1,'Revenue') #zwróci jeden wiersz

the_biggest = pd.DataFrame()
for country, country_data in groups:
    the_biggest = the_biggest.append(country_data.nlargest(1, 'Revenue'))
print(the_biggest)