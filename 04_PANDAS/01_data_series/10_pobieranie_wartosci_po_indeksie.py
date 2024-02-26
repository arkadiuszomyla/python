import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"), usecols=['Name']).squeeze()


print(obj[73])
print(obj[[73, 56, 88]]) #można podać listę
print(obj[2:7]) #5 obiektów, ucina ostatnie
print(obj[795:]) #zwraca wszystko do konca
print(obj[:4]) #wszystko do 4 bez 4
print(obj[-2:]) #szukanie od konca