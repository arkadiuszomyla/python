import matplotlib.pyplot as plt
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

bar = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_barcelona.csv"), index_col='Date')
rom = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_rome.csv"), index_col='Date')
ams = pd.read_csv(os.path.join(parent_directory, "course-files", "weather_amsterdam.csv"), index_col='Date')


temp_max = pd.DataFrame(index=bar.index)
temp_max['Barcelona'] = bar['TempMax']
temp_max['Rome'] = rom['TempMax']
temp_max['Amsterdam'] = ams['TempMax']


def GradeDay(row):
    if(row['TempMax'] >= row['AvgTempMax']):
        return 'PLUS'
    else:
        return 'MINUS'


rom['GradeDay'] = rom.apply(GradeDay, axis=1)
bar['GradeDay'] = bar.apply(GradeDay, axis=1)
ams['GradeDay'] = ams.apply(GradeDay, axis=1)

print(rom['GradeDay'].value_counts())
'''
PLUS     70
MINUS    20
Name: GradeDay, dtype: int64
'''

cities3 = pd.DataFrame(index=['MINUS', 'PLUS'])
cities3['Barcelona'] = bar['GradeDay'].value_counts()
cities3['Rome'] = rom['GradeDay'].value_counts()
cities3['Amsterdam'] = ams['GradeDay'].value_counts()
print(cities3)
'''
       Barcelona  Rome  Amsterdam
MINUS         26    20         22
PLUS          64    70         68
'''

cities3['Barcelona'].plot(kind='pie') #chce zobaczyć dane dotyczące barcelony na wykresie kołowym
cities3['Barcelona'].plot(kind='pie', figsize=(7,7)) #można ustalić rozmiar
plt.show()

#cities3.plot(kind='pie') #zwroci błąd bo wykres kołowy może pokazać dla jednej serii

cities3.plot(kind='pie', subplots=True) #zwróci wykresy dla wszystkich serii obok siebie
plt.show()


cities3.plot(kind='pie', subplots=True, colors=['b', 'g'], labels=['colder', 'warmer'],
             autopct='%.0f%%', fontsize=20, textprops=dict(color='w'),
             layout=(2,2)) #można kolory i zmienić nazwy wartości, i ustawić aby pokazywało wartości procentowe, textprops - zmienia  kolor wartości, layout - ile wykresów poziomo, ile pionowo