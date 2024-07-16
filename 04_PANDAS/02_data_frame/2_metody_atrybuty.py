import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

series = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"), usecols=["Item", "Calories"], index_col="Item").squeeze()
frame = pd.read_csv(os.path.join(parent_directory, "course-files", "mcdonalds.csv"))

print(frame.head())
print(series.head())

print(series.count()) #ile elementów w danej serii - tutaj 260
print(frame.count())  #ile jest znanych elemtów w kolumnie - wartości wygenerowane dla każdej kolumny oddzielnie - 260

print(len(series)) #260, len liczy też wartości NaN, count nie liczy
print(len(frame)) #260

print(series.dtypes) #dtype('int64')
print(frame.dtypes)  #wartości wygenerowane dla każdej kolumny oddzielnie

# Metoda wycofana - jako wartość zawsze przyjmij 1
# series.get_dtype_counts()
#
print(frame.dtypes.value_counts()) #zwroci jak nizej
'''
int64      18
object      3
float64     3
dtype: int64
'''

print(series.shape) #jaki kształ danych, ilu wymiarowe, zwróci (260,)
print(frame.shape) # (260, 24) - wymiar tabeli

print(series.axes) #zwraca info na temat indeksu
'''
[Index(['Egg McMuffin', 'Egg White Delight', 'Sausage McMuffin',
       'Sausage McMuffin with Egg', 'Sausage McMuffin with Egg Whites',
       'Steak & Egg McMuffin', 'Bacon, Egg & Cheese Biscuit (Regular Biscuit)',
       'Bacon, Egg & Cheese Biscuit (Large Biscuit)',
       'Bacon, Egg & Cheese Biscuit with Egg Whites (Regular Biscuit)',
       'Bacon, Egg & Cheese Biscuit with Egg Whites (Large Biscuit)',
       ...
       'Shamrock Shake (Medium)', 'Shamrock Shake (Large)',
       'McFlurry with M&M’s Candies (Small)',
       'McFlurry with M&M’s Candies (Medium)',
       'McFlurry with M&M’s Candies (Snack)',
       'McFlurry with Oreo Cookies (Small)',
       'McFlurry with Oreo Cookies (Medium)',
       'McFlurry with Oreo Cookies (Snack)',
       'McFlurry with Reese's Peanut Butter Cups (Medium)',
       'McFlurry with Reese's Peanut Butter Cups (Snack)'],
      dtype='object', name='Item', length=260)]
      '''
print(frame.axes) #zwraca info na temat indeksu - indeks tutaj nie był określony - zwrocil numeraj elementów i drugą listę opisującą kolumny
'''
[RangeIndex(start=0, stop=260, step=1), Index(['Category', 'Item', 'Serving Size', 'Calories', 'Calories from Fat',
       'TotalFat', 'Total Fat (% Daily Value)', 'Saturated Fat',
       'Saturated Fat (% Daily Value)', 'Trans Fat', 'Cholesterol',
       'Cholesterol (% Daily Value)', 'Sodium', 'Sodium (% Daily Value)',
       'Carbohydrates', 'Carbohydrates (% Daily Value)', 'Dietary Fiber',
       'Dietary Fiber (% Daily Value)', 'Sugars', 'Protein',
       'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)',
       'Calcium (% Daily Value)', 'Iron (% Daily Value)'],
      dtype='object')]
      '''

print(series.index) #zwróci indeksy
'''
Index(['Egg McMuffin', 'Egg White Delight', 'Sausage McMuffin',
       'Sausage McMuffin with Egg', 'Sausage McMuffin with Egg Whites',
       'Steak & Egg McMuffin', 'Bacon, Egg & Cheese Biscuit (Regular Biscuit)',
       'Bacon, Egg & Cheese Biscuit (Large Biscuit)',
       'Bacon, Egg & Cheese Biscuit with Egg Whites (Regular Biscuit)',
       'Bacon, Egg & Cheese Biscuit with Egg Whites (Large Biscuit)',
       ...
       'Shamrock Shake (Medium)', 'Shamrock Shake (Large)',
       'McFlurry with M&M’s Candies (Small)',
       'McFlurry with M&M’s Candies (Medium)',
       'McFlurry with M&M’s Candies (Snack)',
       'McFlurry with Oreo Cookies (Small)',
       'McFlurry with Oreo Cookies (Medium)',
       'McFlurry with Oreo Cookies (Snack)',
       'McFlurry with Reese's Peanut Butter Cups (Medium)',
       'McFlurry with Reese's Peanut Butter Cups (Snack)'],
      dtype='object', name='Item', length=260)
      '''
print(frame.index) #zwróci tylko RangeIndex(start=0, stop=260, step=1)


#series.columns #nie zadziała dla serii
print(frame.columns)
'''
Index(['Category', 'Item', 'Serving Size', 'Calories', 'Calories from Fat',
       'TotalFat', 'Total Fat (% Daily Value)', 'Saturated Fat',
       'Saturated Fat (% Daily Value)', 'Trans Fat', 'Cholesterol',
       'Cholesterol (% Daily Value)', 'Sodium', 'Sodium (% Daily Value)',
       'Carbohydrates', 'Carbohydrates (% Daily Value)', 'Dietary Fiber',
       'Dietary Fiber (% Daily Value)', 'Sugars', 'Protein',
       'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)',
       'Calcium (% Daily Value)', 'Iron (% Daily Value)'],
      dtype='object')
      '''

print(series.values) #wyświetla same wartości
print(frame.values) #wyświetla same wartości, lista list wartości, 260 wewnętrznych list

## Nowa dodana metoda
print(series.info())
'''
<class 'pandas.core.series.Series'>
Index: 260 entries, Egg McMuffin to McFlurry with Reese's Peanut Butter Cups (Snack)
Series name: Calories
Non-Null Count  Dtype
--------------  -----
260 non-null    int64
dtypes: int64(1)
memory usage: 4.1+ KB
None
'''
print(frame.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 260 entries, 0 to 259
Data columns (total 24 columns):
 #   Column                         Non-Null Count  Dtype  
---  ------                         --------------  -----  
 0   Category                       260 non-null    object 
 1   Item                           260 non-null    object 
 2   Serving Size                   260 non-null    object 
 3   Calories                       260 non-null    int64  
 4   Calories from Fat              260 non-null    int64  
 5   TotalFat                       260 non-null    float64
 6   Total Fat (% Daily Value)      260 non-null    int64  
 7   Saturated Fat                  260 non-null    float64
 8   Saturated Fat (% Daily Value)  260 non-null    int64  
 9   Trans Fat                      260 non-null    float64
 10  Cholesterol                    260 non-null    int64  
 11  Cholesterol (% Daily Value)    260 non-null    int64  
 12  Sodium                         260 non-null    int64  
 13  Sodium (% Daily Value)         260 non-null    int64  
 14  Carbohydrates                  260 non-null    int64  
 15  Carbohydrates (% Daily Value)  260 non-null    int64  
 16  Dietary Fiber                  260 non-null    int64  
 17  Dietary Fiber (% Daily Value)  260 non-null    int64  
 18  Sugars                         260 non-null    int64  
 19  Protein                        260 non-null    int64  
 20  Vitamin A (% Daily Value)      260 non-null    int64  
 21  Vitamin C (% Daily Value)      260 non-null    int64  
 22  Calcium (% Daily Value)        260 non-null    int64  
 23  Iron (% Daily Value)           260 non-null    int64  
dtypes: float64(3), int64(18), object(3)
memory usage: 48.9+ KB
None
'''
print('\n')

print(series.value_counts())  #ile razy w serii pojawia się ta sama wartość, tu w serii występują tylko liczby
'''
0      16
340    10
430    10
280     9
250     8
       ..
640     1
800     1
740     1
620     1
810     1
Name: Calories, Length: 78, dtype: int64
'''
print('\n')
print(frame["Category"].value_counts()) #ile razy w frame pojawia się ta sama wartość dla konkretnej kolumny
'''
Coffee & Tea          95
Breakfast             42
Smoothies & Shakes    28
Chicken & Fish        27
Beverages             27
Beef & Pork           15
Snacks & Sides        13
Desserts               7
Salads                 6
Name: Category, dtype: int64'''

print(series.sample()) #losuje i wyświetla jednen Item
'''
Item
Latte (Large)    280
Name: Calories, dtype: int64'''
print(frame.sample(n=3, axis="columns").head()) #tu można podać np. ilość elementów do wylosowania, tu piec pierwszych kolumn
print(frame.sample(n=3)) #tu można podać np. ilość elementów do wylosowania
print(frame.sample(frac=0.02)) #2 procent rekordów, które występują w tym obiekcie frame