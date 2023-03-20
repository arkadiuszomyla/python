class Car:

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, accesories):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.accesories = accesories

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOk))
        print("Painting - ok - {}".format(self.isPaintingOk))
        print("Mechanic - ok - ".format(self.isMechanicOk))
        print("Accessories - {}".format(self.accesories))
        print("---------------")

    # operator iadd odpowiada za plus równa się (+=)
    '''
    def __iadd__(self, other):
        accesories = self.accesories
        accesories.extend(other)
        return Car(self.brand, self.model, self.isAirBagOk,
                   self.isPaintingOk, self.isMechanicOk, accesories)
    '''
    #modyfikujemy metodę aby rozpoznawała czy nie jest dodawany pojedyńczy element
    def __iadd__(self, other):
        if type(other) is list:
            accesories = self.accesories
            accesories.extend(other)
            return Car(self.brand, self.model, self.isAirBagOk,
                       self.isPaintingOk, self.isMechanicOk, accesories)
        elif type(other) is str:
            accesories = self.accesories
            accesories.append(other)
            return Car(self.brand, self.model, self.isAirBagOk,
                       self.isPaintingOk, self.isMechanicOk, accesories)
        else:
            raise Exception("Adding type {} is not valid".format(type(other)))

    #można kupić dwa samochody na raz, lista z dwóch obiektow typu Car
    def __add__(self, other):
        if type(other) is Car:
            return (self, other)
        else:
            raise Exception("Adding type {} to Car is not valid". format(type(other)))

    #tekstowa prezentacja dla obiektu, wyświetli print(car_01)
    def __str__(self):
        return "Brand {}, Model {}".format(self.brand, self.model)


car_01 = Car("Seat", "Ibiza", True, True, True, ["winter tires"])
car_01.GetInfo()

# po dodaniu iadd możemy dodać do akcesoriów
car_01 += ["navigation system", "roof rack"]
car_01.GetInfo()

car_01 += "loudspeeker system"
car_01.GetInfo()

car_02 = Car("Opel", "Astra", True, False, False, [])

car_pack = car_01 + car_02
print("car_01 + car_02", car_pack[0].brand, car_pack[1].brand)

print(car_01)   #<__main__.Car object at 0x000002BD187A7FD0>