class Car:
    #init to konstruktor,ma za zadanie zainicjować obiekt
    #atrybuty
    def __init__(self, brand, model, isAirBagOK, IsPaintingOk, isMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.IsPaintingOk = IsPaintingOk
        self.isMechanicOk = isMechanicOk


#instancje niżej
car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, True, True)

print(car_01.model, car_02.model, car_01.isMechanicOk)