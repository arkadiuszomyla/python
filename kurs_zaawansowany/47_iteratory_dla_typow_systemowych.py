aTuple = (1,2,3,4,5)


#tuple jest iterable
for x in aTuple:
    print(x)

print(next(aTuple))  #ten obiekt jednak nie posiada własnego iteratora

it = iter(aTuple)   #dlatego trzeba iter
print(next(it))
print(next(it))
print(next(it))

''' TAK SAMO JEST Z LISTĄ i ZE ZBIOREM (lista różnych nieuporządkowanych elementów)'''

#file posiada metodę iter i metodę next
with open('c:\\temp\\lines.txt' ,r) as file:
    while True:
        try:
            print(next(file))
        except StopIteration:
            break

