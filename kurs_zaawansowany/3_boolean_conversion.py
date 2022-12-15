isOk = True
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')


isOk = 'Python'
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')      #WYDRUJE TRUE

isOk = 'FALSE'
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')  #WYDRUJE TRUE

isOk = ''
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')  #NIC NIE WYDRUKUJE

isOk = 1
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')  #WYDRUJE TRUE

isOk = 0
print('Variable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')  #NIC NIE WYDRUKUJE