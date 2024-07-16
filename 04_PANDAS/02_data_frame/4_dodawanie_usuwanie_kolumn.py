import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"), usecols=["Item","Category","Calories","TotalFat","Sugars","Protein","Cholesterol"])

print(frame.head())

print(frame.TotalFat.head()) #wartości tylko tej kolumny
print(frame["TotalFat"].head()) #to samo co wyżej, ale też tak można

frame["NowaKolumna"] = 0  #dodaje nową kolumne NowaKolumna o wartości 0

SugarAndFat = frame.Sugars + frame.TotalFat  #dodaje nową kolumne
frame["SugarAndFat"] = SugarAndFat

frame["SugarAndProtein"] = frame.Sugars + frame. Protein #to samo co wyżej w jednej linijce

frame.insert(loc=2, column="SPF", value=frame.Sugars + frame.Protein + frame.TotalFat) #dodaje kolumne na danej pozycji, pozycja, nazwa kolumny, wartość, pozycje liczymy od 0

del frame["SugarAndProtein"] #usuwanie kolumny
#del frame.SugarAndFat  #nie zadziała

frame = frame.drop(columns=["SugarAndFat"]) #usuwa kolumne, metoda frame zwraca obiekt dataframe i trzeba przypisać do nowego

frame.drop(labels="NowaKolumna", axis=1, inplace=True) #axis=1 - usuwamy kolumne, axis=0 - usuwamy wiersze, inplace - powoduje, że metoda nic nie zwraca - powoduje, że modyfikowany jest oryginalny obiekt