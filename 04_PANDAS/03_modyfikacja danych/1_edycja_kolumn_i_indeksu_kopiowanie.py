import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mammals.csv"))

#print(frame)
print(frame.columns) #Index(['name', 'body', 'brain'], dtype='object')
frame.columns = ['name', 'bodyKg', 'brainKg'] #przypisujemy nowe nazwy kolumn

newColumnNames = {'bodyKg': 'body_kg', 'brainKg': 'brain_kg'} #słownik - stara nazwa, nowa nazwa
frame.rename(columns=newColumnNames, inplace=True) #zmieniamy wybrane nazwy, dla oryginalnego obiektu

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mammals.csv"), index_col='name') #importujemy plik jeszcze raz jako index wybierając name
frame.rename(index={'Cow': 'Land cow'}, inplace=True) #stara wartość indeksu, nowa wartość indeksu

frameCopy = frame #kopia obiektu
frameCopy.loc['Arctic fox', 'body'] = 5 #ustawiam wagę lisa na 5
frame.head() #TU TEŻ SIĘ ZMIENIŁO!, to samo miejsce w pamięci

frameCopy = frame.copy()  #trzeba użyć copy, wtedy dane zapisują się w nowych miejscach w pamięci