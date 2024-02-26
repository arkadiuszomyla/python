import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"), usecols=['Name']).squeeze()

type(obj)
len(obj)  #ilość elementów
print(sorted(obj))  #to już lista
dict(obj.head())    #to już słownik

print(min(obj))
print(obj.name) #Name
obj.name = 'Name of pokemon'
print(obj.name)