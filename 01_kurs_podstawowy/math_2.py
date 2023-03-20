import math

f_smaller = 3.14159265335895389
f_bigger = 3.87756392764

print(math.ceil(f_smaller), math.ceil(f_bigger)) #zwraca najmniejszą liczbę całkowitą dla przekazanego argumentu
print(math.floor(f_smaller), math.floor(f_bigger))  #zwraca nawiększą liczbę, która jest zmniejsza od podanego argumentu
print(math.ceil(-f_smaller), math.ceil(-f_bigger))
print(math.floor(-f_smaller), math.floor(-f_bigger))

print(pow(2,8), pow(9,0,5))  #power, potęgowanie, pierwiastki
print(math.sqrt(16))  #pierwiastek kwadratowy


degree = 360
radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree, radian))

degree = 45
radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree, radian))
print('')

print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))
print('')

small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38

small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_area = math.pi * small_pizza_r ** 2
big_area = math.pi * big_pizza_r ** 2
family_area = math.pi * family_pizza_r ** 2

print('small', small_pizza_r, small_pizza_price, small_area)
print('big', big_pizza_r, big_pizza_price, big_area)
print('family', family_pizza_r, family_pizza_price, family_area)
print('')
print('small', small_pizza_price / small_area)
print('big', big_pizza_price / big_area)
print('family', family_pizza_price / family_area)
print('')

math_ls = dir(math)
print(math_ls)