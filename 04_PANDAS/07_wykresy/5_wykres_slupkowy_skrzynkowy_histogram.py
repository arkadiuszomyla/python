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

cities3['Barcelona'].plot(kind='bar')  #wykres słupkowy
plt.show()
cities3['Barcelona'].plot(kind='barh') #wykres słupkowy poziomy
cities3.plot(kind='bar') #zadziała dla wszystkich
cities3.plot(kind='bar', stacked=True)  #nakłada na siebie słupki

temp_max.plot(kind='box') #wykres skrzynkowy
plt.show()

bar['TempMax'].plot(kind='hist') #histogram, domyślnie pokazuje zaookrąglone wartości
plt.show()
bar['TempMax'].nunique() #mamy 18 różnych wartości
bar['TempMax'].plot(kind='hist', bins=18) #ten histogram pokaże wartości dokładnie