import matplotlib.pyplot as plt
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

bar = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_barcelona.csv"), index_col='Date')
rom = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_rome.csv"), index_col='Date')
ams = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_amsterdam.csv"), index_col='Date')


bar.head()
bar.plot()
plt.show()  #wykres domyślny

bar.plot(color=['b','g','r','m','k']) #ustawiamy sobie kolorki rgb

bar.plot(colormap='magma') #korzystamy z predefiniowanego przez matplotlib zestawu koloru
plt.show()

print(plt.style.available) #możemy wyświetlić listę dostępnych stylów dla wykresów
plt.style.use('Solarize_Light2') #ustawiamy styl
bar.plot()
plt.show()