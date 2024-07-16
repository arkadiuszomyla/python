import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "insurance.csv"))

print(frame)
frame.loc[2, 'Claims'] #indeks, kolumna
frame.loc[2, 'Claims'] = 19
frame.loc[2, 'Claims'] = frame.loc[2, 'Claims'] + 1
frame.loc[2, 'Claims'] += 1

frame["Age"] == "<25"  #zwraca serię danych True lub False w zależności czy warunek jest spełniony
isYounger25 = frame["Age"] == "<25"
frame.where(isYounger25) #wartości spełniające warunek zostaną pokazane, reszta NaN
frame.where(isYounger25).dropna() #wartości NaN usunięte
frame[isYounger25] #pokaże od razu wartości, które spełniają warunek na True, tak bezpieczniej

frame.loc[isYounger25, 'Holders'] #dostaniemy wyniki z kolumny Holders tylko dla ludzi młodszych niż 25lat
frame.loc[isYounger25, 'Holders'] = frame.loc[isYounger25, 'Holders'] + 100

frame.loc[isYounger25, 'Holders'] += 1000

frame.loc[isYounger25, 'Holders'] = frame['Holders'] + 100