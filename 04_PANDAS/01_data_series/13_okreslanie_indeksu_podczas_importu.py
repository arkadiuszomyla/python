import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"),usecols=['Attack']).squeeze()
print(obj)  #index zaczyna się od zera

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"),usecols=['Attack', '#'], index_col=['#']).squeeze()
print(obj) #nowa kolumna index

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"),usecols=['Name', 'Attack'], index_col=['Name']).squeeze()
print(obj) #nowa kolumna index