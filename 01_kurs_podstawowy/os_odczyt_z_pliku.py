file = open("c:\\temp\\plik.txt", "r")
content = file.read()
print(content)
file.close()

### odczytywanie pliku bez konieczności zamykania, nie wydajna dla dużych plików
with open("c:\\temp\\plik.txt", "r") as file:
    content = file.read()
    print(content)


### odczytuje plik linijka po linijce, jest dobre dla duzych plikow
with open("c:\\temp\\plik.txt", "r") as file:
    for line in file:
        print(line)

##przetwarzanie czytając daną ilość bajtów
file = open("c:\\temp\\plik.txt", "r")
fragment = file.read(10)  #chcemy przeczytać 10bajtów
while fragment:
    print(fragment)
    print(file.tell(), fragment)   #wyświetla, w którym miejscu w pliku jesteśmy
    fragment = file.read(10)  #jeżeli jeszcze jest coś do czytania, przeczytaj kolejne 10 (10linii)
file.close()





#Naszym zadaniem jest przeczytać ten plik i przetwarzać go linijka po linijce. Zamówienie umieszczone w każdej linii składa się z 3 informacji: nazwa apteki, nazwa leku,
#ilość opakowań leku. Zdarza się, że niektóre zamówienia nie są poprawne i zawierają więcej danych - tutaj wiersz 2.
#W tym zadaniu przetwarzamy ten plik zupełnie ręcznie, ale oczywiście istnieją zdecydowanie lepsze metody na przetwarzanie danych w Pythonie, np. biblioteka PANDAS, której poświęciłem inny kurs.

'''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10'''

file_path = r'c:\temp\data_input\orders.csv'

with open(file_path, "r") as file:
    for line in file:

        line = line.replace('\n', '')
        order = line.split(',')

        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' %
                  (order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!!" % line)

print("Processing finished")