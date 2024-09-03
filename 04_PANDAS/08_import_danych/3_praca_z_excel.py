import pandas as pd
import numpy as np

sheets = pd.read_excel('PC_Vehicles-in-use.xlsx', sheet_name=[1, 2, 3])

type(sheets) #słownik

sheets[2]

sheets = pd.read_excel('PC_Vehicles-in-use.xlsx', sheet_name=['Old Europe', 'New Europe'])

sheets["New Europe"]

excelWriter = pd.ExcelWriter('cars.xlsx')
sheets["Old Europe"].to_excel(excelWriter, index=False, columns=['REGIONS/COUNTRIES', 2010],
                              sheet_name='Old Europe 2010')
sheets["Old Europe"].to_excel(excelWriter, index=False, columns=['REGIONS/COUNTRIES', 2011],
                              sheet_name='Old Europe 2011')
sheets["Old Europe"].to_excel(excelWriter, index=False, columns=['REGIONS/COUNTRIES', 2012],
                              sheet_name='Old Europe 2012')

# Polecenie save jest wycofane, zamist tego używamy close()
# excelWriter.save()
excelWriter.close()

'''Autorzy biblioteki zachęcają jednak, do korzystania z tzw.context managera. Context manager
pozwala otworzyć plik, po czym w komendach umieszczonych w bloku
with można pracować z obiektem context managera, który pozwala wykonywać zapis:

# Jeśli plik ma być utworzony/nadpisany - użyj mode="w"
# Jeśli plik istnieje, i ma być do niego dodany nowy arkusz użyj mode="a"
# Jeśli chcesz nadpisać istniejący arkusz użyj argumentu if_sheet_exists
# if_sheet_exists{‘error’, ‘new’, ‘replace’, ‘overlay’}
'''
with pd.ExcelWriter("cars.xlsx", mode="w") as excelWriter:
    sheets["Old Europe"].to_excel(excelWriter, index=False,
                                  columns=['REGIONS/COUNTRIES', 2010],
                                  sheet_name='Old Europe 2010', )
    sheets["Old Europe"].to_excel(excelWriter, index=False,
                                  columns=['REGIONS/COUNTRIES', 2011],
                                  sheet_name='Old Europe 2011')
    sheets["Old Europe"].to_excel(excelWriter, index=False,
                                  columns=['REGIONS/COUNTRIES', 2012],
                                  sheet_name='Old Europe 2012')
