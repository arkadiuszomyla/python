import os
import time

print("Current directory is:", os.getcwd())

currentDir = os.getcwd()
filename = "result.txt"
fullpath = os.path.join(currentDir, filename)
print("\nThe constructed file path is: ", fullpath)

relativePath = "output.txt"
print("\nThe absolute path is: ", os.path.abspath(relativePath))  # bezwzględna ścieżka do pliku

filepath = r'c:\temp\results.txt'
print("\nThe file name part is: ", os.path.basename(filepath))  # sama nazwa pliku
print("The directory part is: ", os.path.dirname(filepath))  # katalog, w którym plik się znajduje

print("\nIs file existing? ", os.path.exists(filepath))

if os.path.exists(filepath):
    print("\nLast modify date is:", os.path.getmtime(filepath))
    print("last modify date is: ", time.localtime(os.path.getmtime(filepath)))

    print("\nFile size is: ", os.path.getsize(filepath))  # zwraca rozmiar w bajtach

    print("\nIs it a file?", os.path.isfile(filepath))
    print("Is it a dir? ", os.path.isdir(filepath))

    print("\nPath splitted: ", os.path.split(filepath))  # rozdziela ścieżkę na nazwę katalogu i pliku
    print("Only file name part:", os.path.split(filepath[1]))  # jeżeli interesuje nas np. sama nazwa pliku

    print("\nPath splitted into drive:",
          os.path.splitdrive(filepath))  # rozdziela nazwę dysk i ścieżkę dostępu do pliku
    print("Only drive:", os.path.splitdrive(filepath)[0])  # jeżeli interesuje nas tylko nazwa dysku


### sprawdzanie czy plik istnieje
fileIsOk = False

while True:
    filename = input("Podaj ścieżkę pliku: ")

    if os.path.isfile(filename):
        break
    else:
        print("Nieprawidlowa sciezka")

print("ścieżka pliku to %s" % filename)
