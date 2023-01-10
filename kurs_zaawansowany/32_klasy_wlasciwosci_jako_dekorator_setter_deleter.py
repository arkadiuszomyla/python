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

    #IsOnSale = property(__getIsOnSale, __setIsOnSale, None)
    @property
    def isOnSale(self):
        return self.__isOnSale

    #setter musi być napisany po @property, którego dotyczy i mieć taką samą nazwę
    @isOnSale.setter
    def isOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status isOnSale to{}'.format(newIsOnSaleStatus, self.brand))

    #tak samo jak wyżej
    @isOnSale.deleter
    def isOneSale(self):
         self.__isOnSale = None

    @property
    def carTitle(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model).title()


car_01 = Car('Seat', 'Ibiza', True, True, True, False)


print(car_01.isOnSale)

car_01.isOnSale = True
print(car_01.carTitle)
