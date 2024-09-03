import pandas as pd

url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/avia_par_pl/?format=TSV&unzip=true'
routes = pd.read_csv(url, delimiter='\t') #Plik ten jest oddzielany tabulatorami (dzięki ustawieniu delimiter='\t')
print(routes)

#dane w pierwszej kolumnie są zapisane jak csv rozdzielany przecinkami
routes_desc = routes['freq,unit,tra_meas,airp_pr\\TIME_PERIOD'].str.split(',', expand=True) #otrzymujemy dataframe dla wartości rozdzielonych przecinkami
print(routes_desc)
routes_desc.rename({0:'freq', 1: 'uniq', 2: 'tra_meas', 3: 'airport'}, axis=1, inplace=True) #ustawiamy wartość kolumn, axis = 1 - bo kolumny

routes_desc.join(routes) #łączymy dane, wystarczy join bo mamy identyczne indeksy
#routes_desc.drop('freq,unit,tra_meas,airp_pr\\TIME_PERIOD', axis=1, inplace=True) #usuwamy już nie potrzebną kolumnę



######################################
json_link = 'http://www.floatrates.com/daily/chf.json'
pd.read_json(json_link)
print(json_link)
print(json_link.transpose) #chcemy aby kolumny były wierszami
