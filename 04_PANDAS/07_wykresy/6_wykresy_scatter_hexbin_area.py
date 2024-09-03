import matplotlib.pyplot as plt
import pandas as pd
import os
import re

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

autos = pd.read_csv(os.path.join(parent_directory, "course-files", "autos.csv"), encoding='latin-1')

print(autos)


regex = re.compile('.*toyota.*corolla.*', re.IGNORECASE)
filter1 = autos['name'].apply(lambda x: bool(regex.search(x)))
filter2 = autos['price']<12000
filter3 = autos['yearOfRegistration']>=1990
tc = autos[filter1 & filter2 & filter3]

regex = re.compile('.*Audi.*a4.*', re.IGNORECASE)
filter1 = autos['name'].apply(lambda x: bool(regex.search(x)))
filter2 = autos['price']<12000
filter3 = autos['yearOfRegistration']>=1990
audi = autos[filter1 & filter2 & filter3]


tc.plot(kind='scatter', x='yearOfRegistration', y='price') #wykres kropkowy
plt.show()

ax = audi.plot.scatter(x='yearOfRegistration', y='price', color='Blue', label='Audi')
tc.plot.scatter(x='yearOfRegistration', y='price', color='Green', label='Toyota', ax=ax) #parametr ax i metoda scatter pozwalają łączyć wykresy kropkowe
plt.show()


tc.plot.hexbin(x='yearOfRegistration', y='price', gridsize=20, title='Toyota')
audi.plot.hexbin(x='yearOfRegistration',y='price',gridsize=20,title='Audi')


tc_counts = tc['yearofRegistration'].value_counts().sort_index()
audi_counts = audi['yearofRegistration'].value_counts().sort_index()
car_counts = pd.DataFrame(index=tc_counts.index.append(audi_counts.index).unique())
car_counts['Toyota'] = tc_counts
car_counts['Audi'] = audi_counts
car_counts.plot(kind='area')
plt.show()