countries = ['FR', 'US', 'DE', 'RU']
print(countries[1])
countries[1] = 'GB' #zmiana elementu listy, można wyszukiwać od końca (-1)
countries.append('PL') #dodanie elementu
countries.insert(2, 'ES') #wstawienie na konkretnej pozycji
countries.remove("RU") #usuniecie elementu z listy
countries.sort() #sortowanie listy
countries.reverse() #odwrócenie listy
countries.pop(2) #zwraca wartosc pozycji, a nastepnie ją usuwa
countries.index('PL') #sprawdza czy element występuje i zwraca jego miejsce
print(countries.count("PL")) #ile razy występuje w liście
countries.clear() #czysci liste

newList = ['FI', 'SE']
countries.extend(newList) #dodaje do listy


countriesCopy = countries.copy() #kopiuje listę

# tuple - nawiasy okrągłe, nieedytowalna lista
tax = (4, 5, 7)
print(max(tax))
taxList = list(tax) #rzutowanie
taxList.append(30)
newTax = tuple(taxList)

(tax1, tax2, tax3, tax4) = tax #przypisuje wartosci do konkretnych pozycji
print(tax1, tax2, tax3, tax4)

a = 1
b = 10
(a, b) = (b, a) #tupla zamienia wartości

#Distionary
countriesLeaders = {'PL':'Duda', 'US':'Trump'}
print((countriesLeaders['US']))
countriesLeaders['DE'] = 'Merkel' #dodaje element
countriesLeaders.keys() #zwraca klucze, tutaj np 'PL'
countriesLeaders.values() #zwara wartości dla kluczy
countriesLeaders.items() #zwraca kolekcje

countriesLeaders.popitem() #pobiera jeden z elementów, zwraca i usuwa
countriesLeaders.setdefault('FR', 'Macron') #zwraca wartość ,jeżeli nie ma dodaje wartość do listy
countriesLeaders.get("RU") #pobiera wartość dla klucza, ale nie dodaje

newLeaders = {'RU':'Putin', 'DE':'Schulz'}
countriesLeaders.update(newLeaders) #podmienia wartosc, jeżeli jest nowa wartosc dla klucza, ewentualnie dodaje

