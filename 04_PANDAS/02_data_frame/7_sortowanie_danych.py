import numpy as np
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"), usecols=["Item", "Category", "Serving Size", "Calories", "TotalFat"])

frame.sort_values(by="Calories").head() #sortowanie rosnące dla Calories
frame.sort_values(by="Calories", ascending=False).head() #sortowanie malejące dla Calories

#psujemy dane, Calories to int - nie przypisze się tak po prostu NaN - trzeba zmienić type
frame["Calories"] = frame["Calories"].astype("float")
frame.loc[82, "Calories"] = np.NaN

frame.sort_values(by="Calories").tail() #NaN jest domyślnie traktowane jako największe
frame.sort_values(by="Calories", na_position='first') #NaN będzie traktowane jako najmniejsze

frame.sort_values(by=["Category", "Item"]).head(20) #Sortuje po kategorii i nazwie, dla category sortowanie rosnące, dla item domyślnie malejące
frame.sort_values(by=["Category", "Item"], ascending=[True,False]) #Category będzie sortowane rosnąco, Item malejąco


#importujemy plik jeszcze raz, ale indeksem ma być kolumna z nazwą Item
frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"), usecols=["Item", "Category", "Serving Size", "Calories", "totalFat"], index_col=["Item"])

frame.sort_index(ascending=True) #sortujemy index rosnąco