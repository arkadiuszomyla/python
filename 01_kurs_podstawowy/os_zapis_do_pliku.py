filename = 'c:\\temp\\output.txt'

line = 'Europe'

cities = ['London', 'Berlin', 'Paris', 'Warsaw', 'Hadrid', 'Rome']

file = open(filename, 'w')
file.write(line)
file.wite("\n")           #dodaje nową linie
file.writelines(cities)   #doda kolejną linie, liste bez separatorów
for city in cities:       #zapisze wszystko w nowych liniach
    file.write(city+"\n")
file.close()


file = open(filename, 'a') #otwiera plik do ponownej edycji
file = open(filename, 'w+') #plik otwarty i do zapisu i do odczytu, czyści wcześniejszą zawartość po zapisaniu
file = open(filename, 'a+') #plik otwarty i do zapisu i do odczytu, nie czyści wcześniejszą zawartość po zapisaniu




'''
ZADANIE 1
W tym zadaniu napiszesz program, który zapyta użytkownika o adresy www i zapisze je w pliku.
Zaimportuj moduł os
Zadeklaruj pustą listę webaddresses
Poproś użytkownika o wprowadzenie adresu strony www. Wynik zapamiętaj w zmiennej line
Napisz pętlę, która będzie się wykonywać tak długo  póki line nie jest puste, a w tej pętli
Dodaj line do listy webaddresses i ponownie poproś użytkownika o wprowadzenie adresu strony www zapisując ją w zmiennej line
(Kiedy użytkownik będzie chciał zakończyć wprowadzanie adresów wystarczy, że naciśnie ENTER. W tym przypadku zmienna line będzie pusta i pętla while się zakończy. Na tym etapie będziesz już mieć listę webaddresses zawierającą wprowadzone przez użytkownika adresy)
W zmiennej dirname zapamiętaj ścieżkę do katalogu bieżącego
Poproś użytkownika o wprowadzenie nazwy pliku i wynik zapamiętaj w zmiennej filename)
Korzystając z funkcji os.path.join połącz ze sobą dirname i filename zapamiętując wynik w filepath
Otwórz plik znajdujący się pod ścieżką filepath do zapisu. Zmienna wskazująca na plik może nazywać się file
Dla każdego z adresów znajdujących się na liście webaddresses zapisz ten adres dodając do niego znak nowej linii w pliku.
Zamknij plik
(na tym etapie masz plik, którego zawartością są wprowadzone przez użytkownika adresy www)

ZADANIE 2
W tym zadaniu wczytasz i przeanalizujesz plik utworzony w poprzednim zadaniu
Zaimportuj moduł os
Wczytaj od użytkownika ścieżkę dostępu do pliku utworzonego w poprzednim zadaniu. Wynik zapisz w zmiennej filename
Uwaga: ścieżka wprowadzona przez użytkownika mogła wskazywać na nieistniejący plik, dlatego napisz pętlę while, która będzie się wykonywać tak długo aż użytkownik wprowadzi ścieżkę do istniejącego pliku. Możesz w tym celu korzystać z funkcji os.path.isfile
Jeżeli plik nie istnieje to w pętli wyświetl komunikat i poproś o ponowne wprowadzenie poprawnej ścieżki
(na tym etapie masz wczytaną ścieżkę do istniejącego pliku)
Zadeklaruj zmienną webaddresses, która będzie pustą listą
Otwórz plik wskazywany przez filename na odczyt. Wczytuj zawartość pliku linijka po linijce, zamieniaj w tak wczytanej linii znak końca linii (\n) na napis pusty i dodawaj wczytane linie do zmiennej webaddresses
W zależności od sposobu otwarcia pliku, może być wymagane zamknięcie pliku
Dla każdej linijki znajdującej się na liście webaddresses, jeżeli ta linijka kończy się na .pl to wyświetl "adres+...+ jest adresem z Polski" w przeciwnym razie wyświetl "adres ... nie jest adresem z Polski"

ZADANIE 3
Zmodyfikuj zadanie 2 tak, żeby
polskie adresy zostały zapisane do pliku webs_pl.txt a pozostałe adresy do pliku webs_other.txt
nowe pliki mają powstać w tym samym katalogu co wejściowy plik wskazany przez użytkownika (skorzystaj z funkcji os.path.dirname)
zapisując linie do plików dodawaj do nich znak nowej linii'''

#ZADANIE 1

import os

webaddresses = []
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
while line != '':
    webaddresses.append(line)
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

print(webaddresses)
dirname = os.getcwd()
filename = input("Enter the file name (without directory): ")
filepath = os.path.join(dirname, filename)
file = open(filepath, 'w+')
for webaddress in webaddresses:
    file.write(webaddress + "\n")
file.close()

#ZADANIE 2

import os

filename = input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename = input('Enter filename to read: ')
webaddresses = []
with open(filename, 'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n", ''))
for line in webaddresses:
    if line.endswith('.pl'):
        print(line, 'is a polish web page')
    else:
        print(line, 'is not a polish web page')

#ZADANIE 3

import os

filename = input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename = input('Enter filename to read: ')
webaddresses = []
with open(filename, 'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n", ''))
dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname, 'webs_pl.txt')
websPathOther = os.path.join(dirname, 'webs_other.txt')
filePL = open(websPathPL, 'w')
fileOther = open(websPathOther, 'w')
for line in webaddresses:
    if line.endswith('.pl'):
        filePL.write(line + "\n")
    else:
        fileOther.write(line + "\n")
filePL.close()
fileOther.close()