import numpy as np
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"),
                    usecols=["Item", "Category", "Serving Size", "Calories", "TotalFat"])

print(frame['Calories'].rank().head())  #ranking pokazuje w innej serii, ranking przypisuje wartości liczbowe dla liczby wyświetlonych elementów, jeżeli kilka pozycji trafi na jedną pozycje rankingu jest wyliczana średnia wartość pozycji dla tej ilości elementów
'''
0    115.0
1     82.5
2    146.0
3    178.5
4    156.0
Name: Calories, dtype: float64'''

frame['CaloriesRank'] = frame['Calories'].rank()  # dodajemy kolumnę z rankingiem do naszej tabeli

frame.sort_values(by='Calories').head(20)

frame['CaloriesRank'] = frame['Calories'].rank(ascending=False)  #dodajemy kolumnę z rankingiem do naszej tabeli, teraz robimy najbardziej kaloryczne dania

frame.sort_values(by='Calories', ascending=False, inplace=True).head(3) #bierzemy obiekt, sortujemy w kolejności malejącej, w ramach tego obiektu, wyciągamy trzy najbardziej kaloryczne dania
frame.nlargest(n=3, columns='Calories') #dedykowana funkcja, która robi to co wyżej, można sortować po kilku kolumnach
frame.tail(3) #frame jest już posortowane, więc tak wyciągamy trzy najmniej kaloryczne dania
frame.nsmallest(n=3, columns='Calories') #dedykowana funkcja