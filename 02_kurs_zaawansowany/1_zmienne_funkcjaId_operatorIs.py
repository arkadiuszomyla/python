myvar = 'Hello Python'
myvar2 = myvar
print(myvar2, myvar)
print(type(myvar), type(myvar2))
print('Is value the same?', myvar == myvar2)  # True
print('Are the variables the same?', myvar is myvar2) # True, jedno miejsce w pamięci dwie zmienne
print(id(myvar), id(myvar2))  #te same adresy


myvar2 = myvar + '!!'
myvar2 = myvar2[:-2]  # obcinam dwa ostatnie znaki, wartości będą takie same, ale już o innych adresach