from products import *

class Cart:
    def __init__(self):
        self.__productsList = []
        self.__cartValue = 0

    def addProduct(self, product):
        #if isinstance(product, Phone) or isinstance(product, TV): #zadziala dla wszystkich Product
        if isinstance(product, Product):
            if product not in self.__productsList:
                self.__productsList.append(product)

    def __str__(self):
        strData = "\nCart info, products list:"
        for product in self.__productsList:
             strData += "\n - " + str(product)
        strData += "\nCart value = {}".format(self.__cartValue)
        return strData

    def sumValueCart(self):
        for product in self.__productsList:
            self.__cartValue += product.price
        return "Wartosc koszyka to: {}".format(self.__cartValue)


