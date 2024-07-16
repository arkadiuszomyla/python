import numpy as np
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"))

#psujemy dane
frame.loc[1,"TotalFat"] = np.NaN
frame.loc[1,"Saturated Fat"] = np.NaN
frame.loc[2,"Saturated Fat"] = np.NaN
frame.loc[3,"Category"] = np.NaN

frame.fillna(value=0) #zamiast NaN ustawia podaną wartość, przyjmuje też inplace
replaceDefinitionTable = {'Category':'UNKNOWN','TotalFat':0, 'Saturated Fat':0}  #Category = 0 brzmi źle, chcemy inaczej
frame.fillna(value=replaceDefinitionTable)  #zamienia NaN na to co zdefiniowane w słowniku

frame['Category'].fillna(value='UNKWOWN', inplace=True) #inplace bo chcemy zmienić na tym obiekcie na stałe, zmieniamy tylko dla kolumny
frame['TotalFat'].fillna(value=0, inplace=True) #w kolumnie totalfat zmień NaN na 0, zapisz zmiany na orgyginalnym obiekcie
frame['Saturated Fat'].fillna(value=0, inplace=True)


#psujemy dane znów
frame.loc[1,"TotalFat"] = np.NaN
frame.loc[1,"Saturated Fat"] = np.NaN
frame.loc[2,"Saturated Fat"] = np.NaN
frame.loc[3,"Category"] = np.NaN

avgTotalFat = frame["TotalFat"].mean() #wyliczam średnią
frame["TotalFat"].fillna(avgTotalFat, inplace=True) #zamieniam wszystkie NaN na średnią

frame["Saturated Fat"].fillna(method='ffill', inplace=True) #metoda kopiuje do NaN wartość z poprzedniego wiersza