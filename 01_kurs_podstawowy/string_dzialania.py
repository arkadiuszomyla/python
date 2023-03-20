line = "this IS a very STRANGE text"

line.capitalize() #zmienia tekst na rozpoczynający się więlką literą, reszta mała
line.title()  #każde słowo od wielkiej litery
line.upper()
line.lower()
line.swapcase() #małe na duże, duże na małe
line.casefold() #niektore znaki konwertuje na zwykle i zmiejsza czcionke
line.count("e")  #ile razy występuje znak
line.find("e")  #na której pozycji występuje
line.rfind("e") #na której pozycji od prawej
line.index("e") #to samo co find ale jak nie występuje wywala błąd
"e" in line
line.startswith("this") #czy zaczyna się, czułe na wielkość liter
line.endswith("thin") #czy kończy się, czułe na wielkość liter
line = """this is long text
that spans multiple lines"""   #dodaje /n jako enter

import string
string.ascii_letters
string.digits

line.split(" ") #pozwala rozbić napis na listę, wsazać znak rozbicia
"".join(line) #łączy listę w napisy

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

lines = poem.split('\n')

for i in range(8):
    print(lines[i])
    print(lines[i + 8])