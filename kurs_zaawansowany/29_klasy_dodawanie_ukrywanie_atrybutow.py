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


car_01 = Car('Seat', 'Ibiza', True, True, True, True)
car_02 = Car('Opel', 'Corsa', True, True, True, False)

car_01.getInfo()

car_02.__isOnSale = False
car_02._Car__isOnSale = False  #tak się da zmienić
car_02.YearOFProduction = 2005 #dodaje atrybut do instancji klasy
del car_02.YearOFProduction #usuwa atrybut

setattr(car_02, 'TAXI', False)  #pozwala edytować atrybuty
print(hasattr(car_02, 'TAXI'))  #sprawdza czy obiekt posiada atrybut
delattr(car_02, 'TAXI')   #też usuwa atrybut

print(vars(car_02))