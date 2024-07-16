import pandas as pd
import numpy as np
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
frame = pd.read_csv(os.path.join(parent_directory, "course-files", "sleep_time.csv"))

print(frame.head())

del frame["bodywt"]  #usunięcie pojedynczej kolumny

frame.drop(axis=1, columns=['awake', 'brainwt'], inplace=True) #drop pracuje domyślnie na wierszach, axis = 1 - chodzi o kolumny
frame.drop(axis='columns', columns='sleep_cycle', inplace=True) #tak jak wyżej
frame.drop(columns='sleep_rem', inplace=True)  #jeszcze prościej to co wyżej

frame.drop(axis=0, labels=[1, 2], inplace=True) #usuwanie wierszy, usuń wiersze, które w indeksie mają wartość 1 i 2
frame.drop(axis='rows', labels=3, inplace=True) #to samo co wyżej
frame.drop(labels=4, inplace=True) #to samo co wyżej
frame.drop(5, inplace=True) # i jeszcze prościej w przypadku wierszy

frame.head()


# APPEND JUŻ NIEAKTUALNE, UŻYWAMY CONCAT
# frame.append({'name':'Panda4','genus':np.NaN,'vore':np.NaN,'order':np.NaN,'conservation':np.NaN, 'sleep_total':10}, ignore_index=True)

dict = {'name': ['Panda4'], 'genus': [np.NaN], 'vore': [np.NaN], 'order': [np.NaN], 'conservation': [np.NaN], 'sleep_total': [10]}
pd.concat([frame, pd.DataFrame(dict)], ignore_index=True)

subset = frame[0:5] #zapisujemy wiersze od 0 do 5 w nowej zmiennej
pd.concat([frame, subset]) #dodajemy nowe wiersze, zapisywane na koncu
frame = pd.concat([frame, subset]) #zapisujemy jako nasze frame

