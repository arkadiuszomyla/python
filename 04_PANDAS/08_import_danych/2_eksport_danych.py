import pandas as pd
import numpy as np


df_blood = pd.DataFrame({'Group': ['0', '0', 'A', 'A', 'B', 'B', 'AB', 'AB'],
                         'Rh': ['+', '-', '+', '-', '+', '-', '+', '-'],
                         'Population': [31, 6, 32, 6, 15, 2, 7, 1]})

print(df_blood)

df_blood.to_csv('blood.csv')
print(pd.read_csv('blood.csv'))

df_blood.loc[: ,'Population'] /= 100 #dzielimy populacje przez 100, chcemy procenty
df_blood.to_csv('blood_percent.csv', index=False) #nie eksportuj indeksu
print(pd.read_csv('blood_percent.csv'))

df_blood.to_csv('blood_slim.csv', index=False, columns=['Group', 'Rh']) #tylko wybrane kolumny bez indeksu
print(pd.read_csv('blood_slim.csv'))

df_blood.to_csv('blood_slim.csv', index=False, columns=['Group', 'Rh'], sep=';') #tylko wybrane kolumny bez indeksu + znak separatora ;
print(pd.read_csv('blood_slim.csv', sep=';'))  #przy odczycie trzeba podać sep jeżeli sep to nie przecinek

df_blood.to_csv('blood_slim.csv', index=False, columns=['Group', 'Rh'], sep=';', mode='a', header=False) #mode określa czy można edytować, dopisywać itp; nie chcemy też dopisywać drugi raz nagłówka


df_blood.to_json('blood.json')
print(pd.read_json('blood.json'))