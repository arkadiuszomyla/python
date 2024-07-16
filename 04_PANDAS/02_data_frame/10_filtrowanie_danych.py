import numpy as np
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"),
                    usecols=["Item", "Category", "Serving Size", "Calories", "TotalFat"])

print(frame['Calories'] >= 400)  # zwraca indeks i True/False dla całej tabeli
print((frame['Calories'] >= 400).head())
frame['TotalFat'] <= 20

caloriesGreaterEqual400 = frame['Calories'] >= 400
totalFatLessEqual20 = frame['TotalFat'] <= 20
frame[caloriesGreaterEqual400].head()
frame[totalFatLessEqual20].head()

frame[frame['Calories'] >= 400]  # to samo bez przypisywania do nowego obiektu, ale to nieładnie

isBreakfast = frame['Category'] == 'Breakfast'


frame[isBreakfast & caloriesGreaterEqual400] #są śniadaniami i mają więcej niż 400 kalorii
frame[isBreakfast & caloriesGreaterEqual400 & totalFatLessEqual20] #są śniadaniami i mają więcej niż 400 kalorii i mają niską zawartość tłuszczu

frame[~isBreakfast] #pokaż te dania, które nie są śniadaniami

''''''''''''''''''''''''''''''''''''''''''''''''

color = ['green', 'green', 'blue', 'blue', 'red', 'red', 'white']
size = ['S', 'S', 'S', 'M', 'M', 'M', 'L']
gender = ['M', 'W', 'M', 'W', 'M', 'W', 'U']
clothes = pd.DataFrame({'color': color, 'size': size, 'gender': gender})
print(clothes)

isColorBlue = clothes['color'] == 'blue'
isColorGreen = clothes['color'] == 'green'
isColorWhite = clothes['color'] == 'white'
isGenderM = clothes['gender'] == 'M'
isGenderW = clothes['gender'] == 'W'
isGenderU = clothes['gender'] == 'U'
isSizeS = clothes['size'] == 'S'
isSizeM = clothes['size'] == 'M'
isSizeL = clothes['size'] == 'L'

clothes[isColorBlue & isGenderM & isSizeS] #niebieskie, męskie ubranie w rozmiarze S
clothes[isColorBlue | isGenderM | isSizeS] #niebieskie lub męskie lub ma romiar S
clothes[isColorBlue & isGenderM | isSizeM] #niebieskie i męskie lub rozmiar M, nadrzędna jest operacja &
clothes[isSizeM | isColorBlue & isGenderM] #w pierwszej kolejnośći &
clothes[(isSizeM | isColorBlue) & isGenderM] #w rozmiarze M lub niebieskie ale muszą być koniecznie męskie