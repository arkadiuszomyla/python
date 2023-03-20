import csv
import types

#funcja statyczna
# ścieżka, lista nagłówków wartości, lista wartości
def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        # plik, czym rozdzielane, jeżeli są wartości tekstowe zawierające już przecinek to w quotechar czym mają być zamknięte, jak mocno mają być cytowane wartości
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # naglowek
        writer.writerow(header)
        # dane
        writer.writerow(data)
    print('>>> Tris is function exportToFile - static method')

#funkcja na poziomie klasy
def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print('>>> Tris is function exportToFile - class method')

#funkcja na poziomie instancji
def exportToFile_Instance(self, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([self.brand, self.model, self.IsonSale])
    print('>>> Tris is function exportToFile - instance method')

brandOnSale = 'Opel'


class Car:
    numbersOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOk, isMechanicOk, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.__isOnSale = isOnSale
        Car.numbersOfCars += 1
        Car.listOfCars.append(self)

    def isDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOk and self.isMechanicOk)

    def getInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOK))
        print("Painting - ok - {}".format(self.isPaintingOk))
        print("Mechanic - ok {}".format(self.isMechanicOk))
        print("Is on sale - {}".format(self.__isOnSale))
        print("---------------------")

    def __getIsOnSale(self):
        return self.__isOnSale

    def __setIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status isOnSale to{}'.format(newIsOnSaleStatus, self.brand))

    IsOnSale = property(__getIsOnSale, __setIsOnSale, None)


car_01 = Car('Oper', 'Astra', False, False, False, False)
car_02 = Car('Seat', 'Ibiza', True, True, True, True)

print('Static-------' * 10)
exportToFile_Static(r'C\temp\export_static.csv', ['Brand', 'Model', 'IsOnSale'],
                    [car_01.brand, car_01.model, car_01.IsOnSale])

#funcja na poziomie klasy, po Car nowa nazwa
Car.ExportToFile_Static = exportToFile_Static
Car.ExportToFile_Static(r'C\temp\export_static.csv', ['Brand', 'Model', 'IsOnSale'],
                    [car_01.brand, car_01.model, car_01.IsOnSale])
print(dir(Car)) #klasa zawiera teraz funkcje statyczną


print('Class-------' * 10)
#zapisze wszystkie zapamiętane instancje w klasie
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(path=r'C\temp\export_static.csv')
print(dir(Car)) #mamy do dyspozycji funcje statyczną, dla klasy

print('Instance-------' * 10)
# trzeba użyć types, bo inaczej nie zczyta self, tak jak w klasie car_01.ExportToFile_Instance = exportToFile_Instance
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(path=r'C\temp\export_static.csv')
print(dir(car_01))  #mamy do dyspozycji funcje statyczną, dla klasy i instancji


print('-'*50)
#sprawdza czy funkjca jest w intancji i callable sprawdza czy da się ją uruchomić
if hasattr(car_01, 'ExportToFile_Static') and callable(car_01.ExportToFile_Static):
    print('The object has method ExportToFile_Static')
if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print('The object has method ExportToFile_Class')
if hasattr(car_01, 'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print('The object has method ExportToFile_Instance')