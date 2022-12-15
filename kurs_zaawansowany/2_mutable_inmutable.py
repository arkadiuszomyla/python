number = 10
print('Variable numer: ', number, id(number))
number += 2
print('Variable numer: ', number, id(number))

text = 'Africa'
print('Variable numer: ', text, id(text))
text += 'is hot'
print('Variable numer: ', text, id(text))

list = [1,2,3]
print('Variable list', list, id(list))
list.append(4)
print('Variable list', list, id(list))  #identyfikator listy się nie zmienił, lista jest mutable

list2 = list
print('Variable list', list2, id(list2))  #takie same
list2.append(5)
print('Variable list', list, id(list))
print('Variable list', list, id(list))   #element został dodany do list i list2, adresy nadal takie same

#w jaki sposób zrobić kopię listy, aby przy zmianach, te nie nanosiły się na list?
list3 = list.copy()
print('Variable list', list, id(list))
print('Variable list', list3, id(list3))
list3.append(6)
print('Variable list', list, id(list))
print('Variable list', list3, id(list3)) #tutaj już mamy dwa różne identyfikatory pamięci