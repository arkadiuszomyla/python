import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"),
                    usecols=["Item", "Category", "Serving Size", "Calories", "TotalFat"])

has400CalOrMore = frame["Calories"] >= 400

print(has400CalOrMore[:5])

frame.where(has400CalOrMore) #where zwraca NaN jeżeli nie jest spełniony warunek, jak filtrujemy jak w ostatniej lekcji wiersze są pomijane
frame.where(has400CalOrMore).dropna(how='all') #możemy zrobić where, a następnie usunąć wszystkie wiersze gdzie wartości to NaN

frame.query('Category == "Desserts"') #możemy robić zapytania podobnie jak w sqlu
frame.query('Category in ["Dessers", "Beverages"]')
frame.query('Category == "Desserts" and Calories < 200')