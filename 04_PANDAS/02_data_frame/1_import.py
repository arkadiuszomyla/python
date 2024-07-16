import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"))
print(obj)
print(obj.head())
print(obj.tail())

objSelected = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"), usecols=['Item', 'Serving Size', 'Calories from Fat', 'TotalFat'])
print(objSelected.head())

objSelected = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"), usecols=['Item', 'Serving Size', 'Calories from Fat', 'TotalFat'], index_col='Item')
print(objSelected.head())