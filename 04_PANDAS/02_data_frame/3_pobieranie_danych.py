import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

series = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"), usecols=["Item", "Calories"], index_col="Item").squeeze()
frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"))

print(type(frame)) #<class 'pandas.core.frame.DataFrame'>
print(frame.Calories)  #można podać i wyświetlić po prostu nazwę kolumny
print(type(frame.Calories)) #<class 'pandas.core.series.Series'>, czyli można korzystać z tego co w series

print(frame.Calories.mean()) #średnia 368.2692307692308
print(frame.Calories.median()) #środkowa 340.0
print(frame.Calories.max()) #najbardziej kaloryczne

print(frame.Calories.idxmax()) #na którym indeksie największa wartość #82
print(frame.Item[82]) #pobieranie wartości indeksu, Chicken McNuggets (40 piece)
print(frame.Item[frame.Calories.idxmax()]) #to samo co dwie linijki wyżej razem

print(frame['Calories'].head()) #można podać i wyświetlić po prostu nazwę kolumny też w ten sposób

s = frame['Item']
print(s)
print(type(s)) #<class 'pandas.core.series.Series'>
print(s[242]) #Vanilla Shake (Medium)
print(s.loc[242]) #Vanilla Shake (Medium)
print(frame['Item'][242]) #Vanilla Shake (Medium)
print(frame.loc[242]) #pobiera wszystkie dane, czyli jeden wiersz, dla indeksu 242 czyli Vanilla Shake (Medium), zwraca serie
print(frame.loc[242].loc['Item']) #pobierz Item dla indeksu 242, czyli samo Vanilla Shake (Medium)
#frame['242', 'Item'] - tak nie można, tu działa loc
print(frame.loc[242,'Item']) #Vanilla Shake (Medium)
print(frame['Calories'].head()) #wyciąga daną kolumne
print(frame[['Calories', 'TotalFat', 'Sugars']].head()) #wyciąga wartości dla listy kolumn