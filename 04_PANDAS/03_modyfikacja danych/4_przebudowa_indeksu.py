import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mammals.csv"))


frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mammals.csv"), index_col="name") #możemy ustawić przy wczytaniu inaczje nada się automatycznie 0,1,2,3,4...

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mammals.csv")) #wczytujemy ponownie z domyślnym indeksem

frame.set_index('name', inplace=True) #ustawiamy nowy indeks
frame.reset_index(inplace=True) #wracamy do indeksu automatycznego


frame.set_index('brain', inplace=True) #zmieniamy indeks na brain
frame.set_index('name', inplace=True)  #jednak name, USUNĘŁO KOLUMNĘ BRAIN, poprednia wartość indeksu jest usuwana, przed drugą zmianą indeksu należy przywrócić indeks automatyczny


#prawidłowo:
frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mammals.csv"))
frame.set_index('brain', inplace=True)
frame.reset_index(inplace=True)
frame.set_index('name', inplace=True)


frame.loc['Cow'] #przeszukuje po wszystkich indeksach, nawet jak już znajdzie wartość, możemy najpierw posortować dane, a potem szukać
frame.sort_index(inplace=True)
frame.loc['Cow'] #teraz szuka tylko po 12 wierszach

frame['Cat': 'Donkey'] #zwróć wszystko między kotem, a osłem
frame[:'Cat']
frame['A': 'C'] #zwróć wszystkie od A do C