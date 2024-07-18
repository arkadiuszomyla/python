import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
incidents = pd.read_csv(os.path.join(parent_directory, "course-files", "Canadian Railway Crossing Incidents.csv"))

print(incidents)

incidents.set_index("Region").head() #ustawia nowy indeks zamiast domyślnego - ten jest nieunikalny
incidents.set_index(["Region", "EventType"]).head() #możemy ustawić multiindeks, argument w liście

incidents.set_index(["EventType", "Region"], inplace=True) #zmieniamy kolejność budowania indeksu, domyślnie jest inplace=False

incidents.sort_index(inplace=True) #sortuje dane według indeksu

#przy multiindeks indeksy mogą być grupowane, np. jeden Region może zawierać kilka EventType i tak to jest wyświetlane jako pogrubione
#w drugą stronę też działa po posortowaniu

incidents.sort_index(ascending=[True,False], inplace=True) #pierwszy klucz ma być posortowany rosnąco, drugi malejąco