import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sales = pd.read_csv(os.path.join(parent_directory, "course-files", "WA_Sales_Products_2012-14.csv"))

print(sales.info()) #jakie kolumny, ich typy, czy puste, rozmiar
print(sales.describe()) #pokazuje dla kolumn numerycznych gotowe zestawienie count, mean, std, min, 25%, 50%, 75%, max

print(sales['Retailer country'].value_counts()) #zlicza ile razy wystąpiło
print(sales['Retailer country'].nunique())   #21 - mamy dane pochodzące z 21 krajów


countries = sales['Retailer country'].unique()  #przypisujemy unikalne kraje do nowej zmiennej
myOwnGroups = {} #tworzymy słownik grup

for country in countries:
    myOwnSubDataFrame = sales.where(sales['Retailer country'] == country).dropna()
    myOwnGroups[country] = myOwnSubDataFrame

print(myOwnGroups) #otrzymujemy słownik, gdzie: Nazwa miasta: data frame z zawartością dotyczącą kraju
myOwnGroups['Belgium'] #otrzymuje data frame dotyczące tylko Belgii
myOwnGroups['Belgium'].describe()