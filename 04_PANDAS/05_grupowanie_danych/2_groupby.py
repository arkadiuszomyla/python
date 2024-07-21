import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sales = pd.read_csv(os.path.join(parent_directory, "course-files", "WA_Sales_Products_2012-14.csv"))


#by - kolumna lub lista kolumn względem, których ma być wykonane grupowanie
#axis - grupowanie ze względu na wiersze i kolumny
print(sales.groupby(by='Retailer country'))  #tworzy tylko nowy obiekt, nie wyświetla go

groups = sales.groupby(by='Retailer country')
print(type(groups)) #<class 'pandas.core.groupby.generic.DataFrameGroupBy'>

len(groups) #21 krajów
groups.size() #wyświeli listę krajów i ilość wystąpień każdego
groups.first() #zagląda do każdej z grup i dla każdej z grup wyciąga pierwszy wiersz
sales[sales['Retailer country'] == 'Australia'].head(1) #robi to samo co first()
groups.last() #zagląda do każdej z grup i dla każdej z grup wyciąga ostatni wiersz
groups.groups #jakie grupy zostały zidentyfikowane, zwraca słownik, gdzie kluczami są kraje, a wartościami są liczby, które są indeksami do orginalnego obiektu data frame
sales.loc[groups.groups['Belgium']] #to dopiero wyświetli pełną tabele data frame dla Belgii
groups.get_group('Belgium') #to samo co wyżej - najrpościej