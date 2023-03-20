for i in range(10):
    print(i)

list = range(10)
print('List:', type(list))    #class 'range'

list = list(range(10))
print('List:', type(list))    #class 'list'

print(list[5:7])
print(list[-1:0:-1])
print(list[-1::-1]) #całkowita lista odwrócona