import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
incidents = pd.read_csv(os.path.join(parent_directory, "course-files", "Canadian Railway Crossing Incidents.csv"))

incidents.set_index(["Region", "EventType"], inplace=True)  #kolejnosc indeksów ma znaczenie
incidents.sort_index(inplace=True)

#zadaniem polecenia stuck jest wziąć najbardziej wewnętrzny poziom kolumn i przepisać go do wierszy
incidents.stack() #dostajemy tutaj trzeci poziom indeksu gdzie trzeci indeks zawiera wcześniejsze kolumny, forma danych się zmieniła, została zwrócona seria
incidents.stack().to_frame() #zwraca data frame, gdzie jest jedna kolumna, i trzykolumnowy index


stackedIncidents = incidents.stack().to_frame()
stackedIncidents.unstack() #przywraca najbardziej wewnętrzny poziom multiindexu do kolumn, -1 to ostatni index, można podać dowolny istniejący
stackedIncidents.unstack(level = 'Region')    #można też tak, albo podać liste kolumn

stackedIncidents.unstack().stack()