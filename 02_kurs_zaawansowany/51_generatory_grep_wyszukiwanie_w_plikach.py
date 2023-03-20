import os

'''Polecenie  grep  służy   do przeszukiwania tekstu lub przeszukiwania danego pliku pod kątem wierszy zawierających dopasowanie do podanych ciągów znaków lub słów . 
Domyślnie  grep  wyświetla pasujące linie.  Użyj grep, aby wyszukać wiersze tekstu pasujące do jednego lub wielu wyrażeń regularnych i wypisuje tylko pasujące wiersze.'''

path = r'C:\Users\arkadiuszo\PycharmProjects\python_nauka\kurs_zaawansowany'
search_string = 'Ford'
file_extension = '.py'

#walk zwraca trzy wartości
for dir_name, subdirs, filename in os.walk(path):
    print(dir_name, subdirs, filename)


for dir_name, subdirs, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(file_extension):
            fullFileNAme = os.path.join(dir_name, filename)
            for line in open(fullFileNAme):
                if search_string in line:
                    print(filename)

def generate_files(base_dir, file_extension):
    for dir_name, subdirs, filenames in os.walk(base_dir):
        if filename in filenames:
            if filename.endswith(file_extension):
                fullFileNAme = os.path.join(dir_name, filename)
                yield fullFileNAme

def grep_files(search_string, files):
    for file in files:
        with open(file) as text:
            if search_string in text.read():
                yield file

files_generator = generate_files(path, file_extension)

for file in grep_files(search_string, files_generator):
    print(file)