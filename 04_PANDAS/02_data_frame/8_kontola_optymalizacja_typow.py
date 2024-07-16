import numpy as np
import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"), usecols=["Item", "Category", "Serving Size", "Calories", "TotalFat"])

print(frame.dtypes)
'''
Category         object
Item             object
Serving Size     object
Calories          int64
TotalFat        float64
dtype: object
'''
print(frame.info())
'''
RangeIndex: 260 entries, 0 to 259
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Category      260 non-null    object 
 1   Item          260 non-null    object 
 2   Serving Size  260 non-null    object 
 3   Calories      260 non-null    int64  
 4   TotalFat      260 non-null    float64
 dtypes: float64(1), int64(1), object(3)
memory usage: 10.3+ KB
None
 '''
print(frame.info(memory_usage='deep'))
'''
RangeIndex: 260 entries, 0 to 259
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Category      260 non-null    object 
 1   Item          260 non-null    object 
 2   Serving Size  260 non-null    object 
 3   Calories      260 non-null    int64  
 4   TotalFat      260 non-null    float64
dtypes: float64(1), int64(1), object(3)
memory usage: 61.7 KB
None
'''

frame.loc[1, 'Serving Size'] = np.NaN
frame.loc[2, 'Calories'] = np.NaN

print(frame.info(memory_usage='deep'))
'''
RangeIndex: 260 entries, 0 to 259
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Category      260 non-null    object 
 1   Item          260 non-null    object 
 2   Serving Size  259 non-null    object 
 3   Calories      259 non-null    float64
 4   TotalFat      260 non-null    float64
dtypes: float64(2), object(3)
memory usage: 61.6 KB
None
'''

# frame['Calories'].astype('int') #zmienia tym kolumny, w tym przypadku zmiana na tym wyrzuci ValueError
frame['Calories'].fillna(value=0, inplace=True) #możemy np. najpierw zamienić na 0
frame['Calories'] = frame['Calories'].astype('int') #musimy przepisać kolumnę przy zmianie typu aby wartości się apisały na stałe

print(frame['Category'].value_counts()) #ile razy kategorie się powtarzają
'''Coffee & Tea          95
Breakfast             42
Smoothies & Shakes    28
Chicken & Fish        27
Beverages             27
Beef & Pork           15
Snacks & Sides        13
Desserts               7
Salads                 6
Name: Category, dtype: int64
'''

frame['Category'] = frame['Category'].astype('category') #w Pythonie istnieje typ danych 'category', w danych nic się nie zmienia, typ kolumny zmienia się na 'category' i dane zajmująa mniej miejsca
frame['Serving Size'] = frame['Serving Siize'].astype('category') #tak samo jak wyżej, jeszcze mniej miejsca