import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"), usecols=['Name']).squeeze()

print(obj.sort_index())
print(obj.sort_values())

print(obj.sort_values(ascending=False).head()) #sortowanie w drugą stronę
obj = obj.sort_index(ascending=False)
print(obj)

obj2 = obj.sort_index(inplace=True) #zwróci nową kopie obiektu, pamięć jest zajmowana tylko jeden raz, sortowanie listy na stałe