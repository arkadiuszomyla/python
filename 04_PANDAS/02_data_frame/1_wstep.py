import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"),usecols=['Name', 'Attack'], index_col=['Name']).squeeze()
