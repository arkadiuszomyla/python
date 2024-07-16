import pandas as pd
import numpy as np
import os

# 1. Importujemy tylko to, czego potrzebujemy
# 2. Zmieniamy nazwy kolumn na przyjazne dla nas
# 3. Robimy porządek w kolumnach i ustawiamy ich typy. Python prawdopodobnie zinterpretuje dane jako typ object


current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
frame = pd.read_csv(os.path.join(parent_directory, "course-files", "PublicTransitExpenses.csv"), low_memory=False)

print(frame.info(memory_usage='deep')) #memory usage: 30.5 MB,widać też jakie typy danych zostały przypisane do jakich kolumn

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "PublicTransitExpenses.csv"),
                    usecols=['Agency', 'Reporter Type', 'Organization Type', 'Rail (Y/N)', 'Fixed Route (Y/N)',
                             'Service Costs', 'Tires and Tubes', 'Total Operating Expenses', 'Service Area Population']
                    , low_memory=False)

print(frame.info(memory_usage='deep')) #memory usage: 9.5 MB


newColumnNames = {'Agency': 'Agency',
                  'Reporter Type': 'ReporterType',
                  'Organization Type': 'OrgType',
                  'Rail (Y/N)': 'IsRail',
                  'Fixed Route (Y/N)': 'IsFixedRoute',
                  'Service Costs': 'ServiceCost',
                  'Tires and Tubes': 'TiresTubesCost',
                  'Total Operating Expenses': 'TotalExpenses',
                  'Service Area Population': 'Population'
                  }
frame.rename(columns=newColumnNames, inplace=True)


frame['ReporterType'].nunique() #ile w danej kolumnie jest unikalnych wartośći, tutaj 4
frame['ReporterType'].count() #ile wierszy
frame['ReporterType'].value_counts() #jakie dokładnie wartości występują, tu będą cztery inne
frame['ReporterType'] = frame['ReporterType'].astype('category')

print(frame.info(memory_usage='deep')) #memory usage: 8.5 MB

frame['Agency'] = frame['Agency'].astype('category')
frame['OrgType'] = frame['OrgType'].astype('category')

print(frame.info(memory_usage='deep')) #memory usage: 5.3 MB

frame['Population'].fillna(0, inplace=True) #zamieniamy nulle/na na 0
frame['Population'] = frame['Population'].astype(int) #ustawiamy kolumnę jako int
frame[[frame['Population']>0]].head()

print(frame.info(memory_usage='deep')) #memory usage: 5.2 MB

frame['IsRail'].replace(('Y','N'), (True, False), inplace=True) #zmieniamy chary na False, True
frame['IsFixedRoute'].replace(('Y','N'), (True, False), inplace=True) #zmieniamy chary na False, True

print(frame.info(memory_usage='deep')) #memory usage: 4.3 MB

frame['IsRail'].fillna(False, inplace=True) #zamieniamy nulle/na na 0, to decyzja biznesowa
frame['IsFixedRoute'].fillna(False, inplace=True) #zamieniamy nulle/na na 0, to decyzja biznesowa

frame['IsRail'] = frame['IsRail'].astype(bool) #ustawiamy kolumnę jako bool
frame['IsFixedRoute'] = frame['IsFixedRoute'].astype(bool) #ustawiamy kolumnę jako bool

print(frame.info(memory_usage='deep')) #memory usage: 3.2 MB


frame['ServiceCost'] = frame['ServiceCost'].str.replace('$', '') #usuwamy znak dolara, aby ustawić float
frame['TiresTubesCost'] = frame['TiresTubesCost'].str.replace('$', '') #usuwamy znak dolara, aby ustawić float
frame['TotalExpenses'] = frame['TotalExpenses'].str.replace('$', '') #usuwamy znak dolara, aby ustawić float

frame['ServiceCost'] = frame['ServiceCost'].astype('float')
frame['TiresTubesCost'] = frame['TiresTubesCost'].astype('float')
frame['TotalExpenses'] = frame['TotalExpenses'].astype('float')

print(frame.info(memory_usage='deep')) #memory usage: 861.9 KB