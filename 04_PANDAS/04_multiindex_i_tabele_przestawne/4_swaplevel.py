import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
incidents = pd.read_csv(os.path.join(parent_directory, "course-files", "Canadian Railway Crossing Incidents.csv"))

incidents.set_index(["Region", "EventType"], inplace=True)  #kolejnosc indeksów ma znaczenie
incidents.sort_index(inplace=True)

#jeśli coś jest indeksem to nie jest kolumną w ścisłym znaczeniu obiektu dataframe
#incidents.set_index(["EventType", "Region"], inplace=True) #zwróci błąd

incidents.reset_index(inplace=True) #resetujemy indeks
incidents.set_index(["EventType", "Region"], inplace=True) #zmieniamy indeksy
incidents.sort_index(inplace=True)

incidents.swaplevel().sort_index()  #bez parametrów zmienia kolejność dwóch najgłębszych indeksów
incidents = incidents.swaplevel().sort_index()  #swaplevel nie przyjmuje inplace