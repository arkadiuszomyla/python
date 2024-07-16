import numpy as np
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"))

#psujemy dane
frame.loc[1,'Calories']=np.NaN
frame.loc[2,'TotalFat']=np.NaN

frame.dropna() #zwraca dataframe bez wierszy gdzie jest jakaś wartość NaN

frame.dropna(how='all').head() #how='all' powoduje, że usunięte będą tylko te pozycje, dla których wszystkie wartości to NaN
frame.dropna(subset=["TotalFat"], how='all').head() #subset - jeżeli znajdziesz w tej liście kolumn wartości, które są NaN to usuń wiersz
frame.dropna(axis='rows').head() #axis odpowiada za to czy analizować wiersze czy kolumny, 0-wiersz, 1-kolumna - usuwa wiersze gdzie wystąpi NaN
frame.dropna(axis='columns').head() #axis odpowiada za to czy analizować wiersze czy kolumny, 0-wiersz, 1-kolumna - usuwa kolumny gdzie wystąpi NaN
frame.dropna(inplace=False).head() #zwraca nowy obiekt
frame.dropna(inplace=True).head() #zmiana dokona się bezpośrednio na frame