import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sales = pd.read_csv(os.path.join(parent_directory, "course-files", "WA_Sales_Products_2012-14.csv"))

groups = sales.groupby(by='Retailer country')

groups.mean() #średnie wyniki sprzedaży dla poszczególnych grup, zwraca data frame gdzie wiersze to kraje, a w kolumnach tylko te kolumny gdzie wartosci byly numeryczne
groups.sum() #suma, tak jak wyżej
groups.count() #ilość obiektów występujących w poszczególnych kolumnach w poszczególnych grupach, liczy dla wszystkich kolumn
groups.min() #wartości minimalne dla każdej grupy, dla wszystkich kolumn
groups.max() #wartości maksymalne dla każdej grupy, dla wszystkich kolumn
sales.loc[(sales['Retailer country'] == 'Australia') & (sales['Order method type'] == 'Web')].head() #min i max działa w poszczególnych kolumnach, nie dla rekordu

groups['Revenue'].sum() #możemy sumować tylko dla konkretnej kolumny, albo dla listy kolumn
groups[['Revenue', 'Quantity']].mean()