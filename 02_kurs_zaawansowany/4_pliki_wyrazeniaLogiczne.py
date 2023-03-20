import os
path = r'c:\temp\mydata.txt'  # r - surowy ciąg

#os.remove(path)

'''
if os.path.isfile(path):
    print('File %s exists' % path)
else:
    print('Creating a file %s' % path)
    open(path, 'x').close()        #otwarty i natychmiast zamknięty, x -jeżeli plik istnieje zgłoś błąd
    print('File %s created' % path)

'''

result = os.path.isfile(path) or open(path, 'x').close()  #sprawdź czy plik istnieje lub utwórz plik
print(result)    #True albo False albo None