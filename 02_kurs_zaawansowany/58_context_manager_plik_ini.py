import os


class ini_file:

    def __init__(self, path):
        print('--init--')
        self.path = path
        self.parameters = {}
        self.read_from_disk()

    def read_from_disk(self):
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    parts = line.replace("\n", '').split('=')  #dzielimy linie ze względu na znak '=', spodziewamy się nazwa parametru = wartość parametru
                    self.parameters[parts[0]] = parts[1]       # parametry chcemy przechowywać w słowniku

    def read_parameter(self, key):
        if key in self.parameters.keys():
            return self.parameters[key]
        else:
            return None

    def write_parameter(self, key, value):
        self.parameters[key] = value

    def save_on_disk(self):
        with open(self.path, 'w') as file:
            for key, value in self.parameters.items():
                line = "{}={}\n".format(key, value)
                file.writelines(line)

    def __enter__(self):
        print('--enter--')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('--exit--')
        pass


ini = ini_file(r'c:\temp\my.ini') #tworzę nowy obiekt
ini.write_parameter('varsion', 1) #zapisuje jeden paramentr i drugi
ini.write_parameter('level', 'advenced')
ini.save_on_disk()                #dopiero tutaj zapisuje się na dysku

#aby odczytać muszę stworzyć nowy obiekt
ini2 = ini_file(r'c:\temp\my.ini')   #ponieważ plik teraz istnieje, zostanie on wczytany
print(ini2.parameters)
print(ini2.read_parameter('version'))
print(ini2.read_parameter('level'))


with ini_file(r'c:\temp\my.ini') as ini3:   #tutaj potrzebna jest metoda enter
    print(ini3.parameters)
    print(ini3.read_parameter('version'))
    print(ini3.read_parameter('level'))
