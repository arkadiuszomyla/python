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

#zakładamy klasę Truck, która ma dziedzic/posiadać wszystko co klasa Car

class Truck(Car):
    def __init__(self, brand, model, isAirBagOK, isPaintingOk, isMechanicOk, isOnSale, capacityKg):
        #funkcja super odwołuje się do instancji klasy rodzicielskiej, tutaj Car
        super().__init__(brand, model, isAirBagOK, isPaintingOk, isMechanicOk, isOnSale)
        self.capacityKg = capacityKg

    #wywolujemy najpierw metodę z klasy rodzicielskiej, w praktyce wykona się nadpisana metoda z tej klasy
    def getInfo(self):
        super().getInfo()
        print("CapacityKg - {}".format(self.capacityKg))

truck_01 = Truck("Ford", "Transit", True, True, True, False, 3600)
truck_02 = Truck("Reanult", "Trafic", True, True, True, True, 4800)

print("Calling properties:")
print(truck_01.brand, truck_01.model, truck_01.capacityKg, truck_02.brand, truck_02.model, truck_02.capacityKg)

'''
# mamy metody klasy Car, getInfo bez capacityKg, chyba że w Truck zrobimy getInfo, wtedy tylko ta z Truck
truck_01.getInfo()
truck_02.getInfo()
'''

truck_01.getInfo()