brandOnSale = 'Opel'


class Car:
    '''
    Car - class operating on cars available in the dealer
    '''
    numbersOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOk, isMechanicOk, isOnSale):
        """
        :param brand: the brand of the car
        :param model: the model of the car
        :param isAirBagOK: is the AirBad  not used
        :param isPaintingOk: is the car paint original/no corrections
        :param isMechanicOk: is the car free of any mechanics failure
        :param isOnSale: is the sac covered extra promotion (some additional apply)
        """
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
        """IsOnSale - the car is on extra promotion that is limited is time (only selected cars may be "On Sale\""""
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


#wyświetlanie opisu z komentarzami
help(Car)
help(Car.isOneSale)