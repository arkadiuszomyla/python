import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"), usecols=['Name']).squeeze()

countries = ['EN', 'FR', 'PL', 'IT']

'PL' in countries #True
'ES' in countries #False

'Charmander' in obj #False
3 in obj #True - in sprawdza wartość dla indeksu
3 in obj.index

'Charmander' in obj.values #True