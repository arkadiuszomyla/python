import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
incidents = pd.read_csv(os.path.join(parent_directory, "course-files", "Canadian Railway Crossing Incidents.csv"))

incidents.set_index(["Region", "EventType"], inplace=True)
incidents.sort_index(inplace=True)

print(incidents.head(10))

print(incidents.loc[('Alberta', 'Accidents')]) #jakie były wypadki w Albercie
print(incidents.loc[('Alberta')]) #w przypadku multiindexu nadal możemy przekazać do wyszukiwania jedną wartość, zwraca dataframe z kluczem EventType
print(incidents.loc['Alberta']) #działa też bez nawiasu

print(incidents.iloc[2]) #zwraca pozycje w indeksie

print(incidents.loc[('Alberta', 'Accidents')].loc['Public passive']) #zwróć mi wypadki w Albercie, które są public passive
print(incidents.loc[('Alberta', 'Accidents'), 'Public passive']) #to samo co wyżej, ale prościej

#pomyśl o loc jako o poleceniu, które szuka współrzędnej komórki; idendyfikator wiersza i nazwa kolumny wskazuje wartość