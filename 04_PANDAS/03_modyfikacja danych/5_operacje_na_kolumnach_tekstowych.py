import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "PublicTransitExpenses.csv"),
                    usecols=["Agency", "Reporter Type", "Total Operating Expenses"])

print(frame)
frame['Agency'].str.contains('washington')  # True tam gdzie występuje lub False, wrażliwe na wielkość liter
frame['Agency'] = frame['Agency'].str.lower()  # wstawiamy małe litery
frame['Agency'].str.lower()  # można wykonywać w locie

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "PublicTransitExpenses.csv"),
                    usecols=["Agency", "Reporter Type", "Total Operating Expenses"])  # wracamy

frame[frame['Agency'].str.lower().str.endswith('ferries')]  # zalecane jest dodanie zmiennej
endsWithFerries = frame['Agency'].str.lower().str.strip().endswith(
    'ferries')  # strip wyrzuca spacje na początku i końcu
frame[endsWithFerries]

frame.set_index('Agency', inplace=True)
frame.index = frame.index.str.strip().str.upper()

frame["Reporter Type"].value_counts()  # zlicza wystapienia

frame["Reporter Type"].str.split(
    ' ')  # zwraca obiekt serii danych - indeks, tutaj Agency, oraz wartości, które są listami tutaj stringów, które były rozdzielone spacjami
frame["Reporter Type"].str.split(' ').str[0]  # zwróci tylko pierwszą pozycje z wartości listy
frame["Reporter Type"].str.split(' ',
                                 expand=True)  # expand powoduje, że zostaną zwrócone dodatkowe kolumny zamiast zamiast kolumny z listą
frame["ReporterType1", "ReporterType2"] = frame["Reporter Type"].str.split(' ',
                                                                           expand=True)  # dodajemy kolumny do naszego framea

frame['Agency 2'] = frame.index  # przepisujemy wartości z indeksu do innej kolumny (chcemy przetestować więcej spacji)
frame['Agency 2'].str.split(' ', expand=True, n=10)  # doda 11 kolumn sprawdzając czy są spacje


def getComment(row): #przyjmuje wiersz
    reporterType = row['Reporter Type']   #wez wartosc kolumny
    cost = float(row['Total Operating Expenses'].replace('%', ''))  #wyrzucamy $ z Total Operating Expenses

    if (cost > 20000):
        comment = 'CLASS A'
    else:
        comment = 'CLASS B'
    return (reporterType + '/' + comment)


frame.apply(getComment, axis=1) #najpierw nazwa funkcji, potem czy dla każdego indeksu czy dla każdej kolumny