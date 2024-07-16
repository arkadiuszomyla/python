import numpy as np
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"),
                    usecols=["Item", "Category", "Serving Size", "Calories", "TotalFat"])


color = ['green', 'green', 'blue', 'blue', 'red', 'red', 'white']
size = ['S', 'S', 'S', 'M', 'M', 'M', 'L']
gender = ['M', 'W', 'M', 'W', 'M', 'W', 'U']
clothes = pd.DataFrame({'color': color, 'size': size, 'gender': gender})

isColorBlue = clothes['color'] == 'blue'
isColorGreen = clothes['color'] == 'green'
isColorWhite = clothes['color'] == 'white'
isGenderM = clothes['gender'] == 'M'
isGenderW = clothes['gender'] == 'W'
isGenderU = clothes['gender'] == 'U'
isSizeS = clothes['size'] == 'S'
isSizeM = clothes['size'] == 'M'
isSizeL = clothes['size'] == 'L'


clothes[isColorBlue | isColorGreen | isColorWhite] #pobierz wrzystkie kolory
clothes[clothes['color'].isin(['blue', 'green', 'white'])] #to samo, jak in z sql

myColors = clothes['color'].isin(['blue', 'green', 'white'])
clothes[myColors]  #to samo co wyżej, ale ładniej


clothes.loc[6,'size'] = np.NaN #psujemy dane

clothes['size'].notnull() #zwraca True jeśli nie null, False jeśli null
hasSize = clothes['size'].notnull()
clothes[hasSize]  #zwróci tylko to co ma określony rozmiar

clothes['size'].isnull()  #zwraca False jeśli nie null, True jeśli null
sizeUnknown = clothes['size'].isnull()
clothes[sizeUnknown] #zwróci tylko to co nie ma określonego rozmiar


hasMoreThan300Cal = frame['Calories'] >= 300
hasLessThan400Cal = frame['Calories'] <= 400

frame[hasMoreThan300Cal & hasLessThan400Cal] #łączymy warunki
caloriesBetween300and400 = frame["Calories"].between(300, 400) #lub używamy between
frame[caloriesBetween300and400]