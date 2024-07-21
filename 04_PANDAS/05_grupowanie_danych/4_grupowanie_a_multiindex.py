import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sales = pd.read_csv(os.path.join(parent_directory, "course-files", "WA_Sales_Products_2012-14.csv"))

groups = sales.groupby(by=['Retailer country', 'Year'])
groups.size() #zwraca ilości wierszy pogrupowane dla krajów i roków, tak jakby były dwa indeksy, reszta metod będzie działać tak samo
groups.sum()

print(groups.get_group(('Australia', '2012'))) #dane odpowiadające za Australie z 2012 roku, wpisujemy w tuple