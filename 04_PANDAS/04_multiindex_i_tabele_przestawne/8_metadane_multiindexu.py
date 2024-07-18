import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
incidents = pd.read_csv(os.path.join(parent_directory, "course-files", "Canadian Railway Crossing Incidents.csv"))

incidents.set_index('Region', inplace=True) #ustawiamy jeden indeks
print(incidents.index)
'''
Index(['Newfoundland', 'Newfoundland', 'Newfoundland', 'Nova Scotia',
       'Nova Scotia', 'Nova Scotia', 'New Brunswick', 'New Brunswick',
       'New Brunswick', 'Quebec', 'Quebec', 'Quebec', 'Ontario', 'Ontario',
       'Ontario', 'Manitoba', 'Manitoba', 'Manitoba', 'Saskatchewan',
       'Saskatchewan', 'Saskatchewan', 'Alberta', 'Alberta', 'Alberta',
       'British Columbia', 'British Columbia', 'British Columbia',
       'Northwest Territories', 'Northwest Territories',
       'Northwest Territories'],
      dtype='object', name='Region')
'''
incidents.reset_index(inplace=True)
incidents.set_index(['Region', 'EventType'], inplace=True)
print(incidents.index)
'''
MultiIndex([(         'Newfoundland',        'Accidents'),
            (         'Newfoundland',       'Fatalities'),
            (         'Newfoundland', 'Serious injuries'),
            (          'Nova Scotia',        'Accidents'),
            (          'Nova Scotia',       'Fatalities'),
            (          'Nova Scotia', 'Serious injuries'),
            (        'New Brunswick',        'Accidents'),
            (        'New Brunswick',       'Fatalities'),
            (        'New Brunswick', 'Serious injuries'),
            (               'Quebec',        'Accidents'),
            (               'Quebec',       'Fatalities'),
            (               'Quebec', 'Serious injuries'),
            (              'Ontario',        'Accidents'),
            (              'Ontario',       'Fatalities'),
            (              'Ontario', 'Serious injuries'),
            (             'Manitoba',        'Accidents'),
            (             'Manitoba',       'Fatalities'),
            (             'Manitoba', 'Serious injuries'),
            (         'Saskatchewan',        'Accidents'),
            (         'Saskatchewan',       'Fatalities'),
            (         'Saskatchewan', 'Serious injuries'),
            (              'Alberta',        'Accidents'),
            (              'Alberta',       'Fatalities'),
            (              'Alberta', 'Serious injuries'),
            (     'British Columbia',        'Accidents'),
            (     'British Columbia',       'Fatalities'),
            (     'British Columbia', 'Serious injuries'),
            ('Northwest Territories',        'Accidents'),
            ('Northwest Territories',       'Fatalities'),
            ('Northwest Territories', 'Serious injuries')],
           names=['Region', 'EventType'])

Process finished with exit code 0
'''
print(incidents.index.get_level_values(0))
'''
Index(['Newfoundland', 'Newfoundland', 'Newfoundland', 'Nova Scotia',
       'Nova Scotia', 'Nova Scotia', 'New Brunswick', 'New Brunswick',
       'New Brunswick', 'Quebec', 'Quebec', 'Quebec', 'Ontario', 'Ontario',
       'Ontario', 'Manitoba', 'Manitoba', 'Manitoba', 'Saskatchewan',
       'Saskatchewan', 'Saskatchewan', 'Alberta', 'Alberta', 'Alberta',
       'British Columbia', 'British Columbia', 'British Columbia',
       'Northwest Territories', 'Northwest Territories',
       'Northwest Territories'],
      dtype='object', name='Region')
'''
print(incidents.index.get_level_values(1))
'''
Index(['Accidents', 'Fatalities', 'Serious injuries', 'Accidents',
       'Fatalities', 'Serious injuries', 'Accidents', 'Fatalities',
       'Serious injuries', 'Accidents', 'Fatalities', 'Serious injuries',
       'Accidents', 'Fatalities', 'Serious injuries', 'Accidents',
       'Fatalities', 'Serious injuries', 'Accidents', 'Fatalities',
       'Serious injuries', 'Accidents', 'Fatalities', 'Serious injuries',
       'Accidents', 'Fatalities', 'Serious injuries', 'Accidents',
       'Fatalities', 'Serious injuries'],
      dtype='object', name='EventType')
'''
print(incidents.index.names)  # ['Region', 'EventType']
incidents.index.set_names(['Area', 'Event'], inplace=True)  #zmieniamy nazwy indeksów