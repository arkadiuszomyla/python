from cart import *

phone1 = Phone("TELEFON", 200, 200)
tv1 = TV('TW', 200, 200)

cart = Cart()
cart.addProduct(phone1)
cart.addProduct(tv1)

print(cart.sumValueCart())
print(cart)
