import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
incidents = pd.read_csv(os.path.join(parent_directory, "course-files", "Canadian Railway Crossing Incidents.csv"))

incidents.set_index(["Region", "EventType"], inplace=True)
incidents.sort_index(inplace=True)

incidents.count() #mamy 4kolumny i 30wierszy

incidents.transpose() #zamienia na 30kolumn i 4wiersze; transpose nie posiada parametru inplace

events = incidents.transpose() #transpose nie posiada parametru inplace, można ewentualnie zapisać wynik do innej zmiennej

events.loc['Private'] #wyświetl tylko wypadki na prywatnych przejściach, tylko jeden wiersz ma wartość private

print(events) #indeks składa się z jednej kolumny 'EvantType', nazwy kolumn składają się z dwóch wartości
events.loc['Public passive',('Manitoba', 'Accidents')]
events.iloc[0,5] #wiersz 0, kolumna 5

events.traspose() #wracamy do pierwowzoru