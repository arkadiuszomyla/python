import pandas as pd
import matplotlib.pyplot as plt
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

bar = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_barcelona.csv"), index_col='Date')
rom = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_rome.csv"), index_col='Date')
ams = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_amsterdam.csv"), index_col='Date')

bar['TempMax'].plot()
plt.show()

bar.plot(y='TempMax') #to samo, ale legenda nazwana
bar[['TempMax', 'TempMin']] #jak chce pobrać tylko dwie zmienne

bar[['TempMax', 'TempMin']].plot()   #wystarczy dodać plot()
plt.show()

bar.plot(y=['TempMax','TempMin']) #to samo, ale legenda nazwana
