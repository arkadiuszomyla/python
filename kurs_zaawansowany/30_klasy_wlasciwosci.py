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
        #definiuje coś co jest wewnętrzne, nie można potem go ustawić, ukrywa na zewnątrz
        self.__isOnSale = isOnSale
        Car.numbersOfCars +=1
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

    #parametry: metoda pozwalająca pobrać, metoda pozwalająca ustawić, metoda pozwalająca usunąć, ukryty argument pozwala zapisać dokumentacje
    IsOnSale = property(__getIsOnSale, __setIsOnSale, None)


car_01 = Car('Seat', 'Ibiza', True, True, True, True)
car_02 = Car('Opel', 'Corsa', True, True, True, False)

print("Status of cars:", car_01.getIsOnSale(), car_02.getIsOnSale())
car_01.setIsOnSale(True) #wyrzuci błąd bo to nie opel
car_02.setIsOnSale(False)
print("Status of cars:", car_01.getIsOnSale(), car_02.getIsOnSale())

car_01.IsOnSale = True
car_02.IsOnSale = False