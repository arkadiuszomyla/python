import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sales = pd.read_csv(os.path.join(parent_directory, "course-files", "WA_Sales_Products_2012-14.csv"))

groups = sales.groupby(by=['Retailer country', 'Year'])

groups['Revenue'].sum()
groups['Quantity'].sum()
groups['Gross margin'].mean()

groups.Revenue.sum()  #kolumna bez spacji w nazwie staje się 'właściwością' grupy
groups.Quantity.sum()
#dla Gross margin nie zadziałała bo jest spacja

groups.agg({'Revenue': 'sum'}) #jako parametr podajemy słownik gdzie kluczem jest kolumna, a wartością nazwa funkcji, która ma być wykonana dla kolumny
groups.agg({'Gross margin': 'mean'}) #można ze spacją

groups.agg({'Revenue': 'sum',
            'Quantity': 'sum',
            'Gross margin': 'mean'
            })

groups.agg({'Revenue': ['sum', 'min', 'max'],
            'Quantity': ['sum', 'min', 'max'],
            'Gross margin': 'mean'
            })

my_aggregation = ['sum', 'min', 'max']
groups.agg({'Revenue': my_aggregation,
            'Quantity': my_aggregation,
            'Gross margin': 'mean'
            })