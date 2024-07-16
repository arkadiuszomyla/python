import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"),usecols=['Name', 'Attack'], index_col=['Name']).squeeze()

print(obj.count()) #ile danych

pokType = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"),usecols=['Name', 'Type 2'], index_col=['Name']).squeeze()

print(pokType.head())
print(pokType.value_counts()) #ile poszczególnych wartości #sort, ascending

print(obj.min()) #5
print(obj.max()) #190
print(obj.idxmin()) #na którym indeksie minimalna # Chansey
print(obj.idxmax()) #na któym indeksie maksymalna wartość
print(obj.loc[obj.idxmin()]) #5
print(obj.mean()) #79.00125  #średnia
print(obj.sum()) #63201
print(obj.median()) #75.0 środkowa liczba w zbiorze wartości, połowa większa, połowa mniejsza
print(obj.std()) #32.45736586949845 #odchylenie standardowe #rozrzut danych w serii
print(obj.sum() / obj.count()) #79.00125