#eval pozwala pobrać od użytkownika jakiś napis, który to będzie prawdopodobnie fragmentem kodu i ten fragment będzie samodzielnie uruchomić w pythonie

var_x = 10
password = 'My super secret password'

source = 'var_x + 2'

result = eval(source)
print(result)   #zwraca 12

#print(globals())    #globals pozwoli się odwołać do wszystkich obiektów, które występują w każdej sesji pythona, i zobaczysz wszsytkie zdefiniowane zmienne

source = 'password'

globals = globals().copy()
del globals['password']     #usuwam jeżeli jest wprowadzone hasło
#globals = () #srodowisko jest puste
result = eval(source, globals)
print(result)