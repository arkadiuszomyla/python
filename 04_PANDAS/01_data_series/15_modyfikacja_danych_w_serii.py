import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"),usecols=['Name', 'Attack'], index_col=['Name']).squeeze()

print(obj.head())
print(obj*100) #zwraca serie

obj = pd.read_csv(os.path.join(parent_directory, "course-files", "pokemon.csv"),usecols=['Name', 'Type 1'], index_col=['Name']).squeeze()
print(obj.str.upper())  #wartości serii wielkimi literami #przy modyfikacji stringow trzeba dodać str

#nazwa typu pokemona wielkimi literami i poprzedzona z przodu napisem 'Type: '
print('Type: ' + obj.str.upper())
pokType = ('Type: ' + obj.str.upper())


def ReplaceType(oldType):
    if oldType == 'Grass' or oldType == 'Ground':
        return 'Nature'
    else:
        return oldType

print(obj.apply(ReplaceType))  #jeżeli chcemy wywołać funkcje na każdym elemencie serii musimy użyć apply
print(obj.get('Grass'))
print(obj.get('Bulbasaur'))
print(obj.where(obj == 'Grass').dropna())


#chcemy znowu zmienić wartości na wielkie litery, ale nie chcemy pisać funkcji
print(obj.apply(lambda aText: aText.upper()))