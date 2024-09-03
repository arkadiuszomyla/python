import matplotlib.pyplot as plt
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

bar = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_barcelona.csv"), index_col='Date')
rom = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_rome.csv"), index_col='Date')
ams = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_amsterdam.csv"), index_col='Date')


temp_max = pd.DataFrame(index=bar.index)
temp_max['Barcelona'] = bar['TempMax']
temp_max['Rome'] = rom['TempMax']
temp_max['Amsterdam'] = ams['TempMax']
print(temp_max.head()) #zapisaliśmy temperatury w miastach na poszczególne dni

temp_max.plot()
plt.show() #wykres numer 1

temp_max.plot(figsize=(15,5)) #możemy ustawić wielkość wykresu; x, y
plt.show() #wykres numer 2

temp_max.plot(figsize=(15,5), subplots=True) #subplots generuje osobne wykresy (tutaj trzy)
plt.show() #wykres numer 3

temp_max.plot(figsize=(15,5), use_index=False) #wykres nie będzie korzystał z indeksu, tutaj daty, indeks jest stosowany w osi x

temp_max.plot(figsize=(15,5), title='Max temperature by city') #dodanie tytułu do wykresu
plt.show() #wykres numer 4

temp_max.plot(figsize=(15,5), legend=False) #wyłączenie legendy
temp_max.plot(figsize=(15,5), logy=True) #zmiana skali wyświetlania wartości na logarytmiczną

temp_max[:14] #pobranie pierwszych 14 wartośści
temp_max[:14].plot(figsize=(15,5), xticks=(range(14)), rot=45) #wyświetla wartości z indeksu na osi x, rot - pod jakim kątem wyświetlić te wartości
plt.show() #wykres numer 5

temp_max[:14].plot(figsize=(15,5), table=True) #umieszcza pod wykresem tabelke z dokładnymi wartościami widocznymi na wykresie
plt.show() #wykres numer 6