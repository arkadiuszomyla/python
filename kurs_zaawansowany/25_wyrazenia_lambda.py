def double(x):
    return x * 2

x = 10
x = double(x)
print(x)

x = 10
f = lambda x: x * 2    #funkcja anonimowa
print(f(x))


def power(x,y):
    return x ** y   #x do potegi y

x = 5
y = 3
print(power(x,y))

x = 5
y = 3
f = lambda x, y: x ** y
print(f(x,y))

list_number = [1, 2,3, 4, 11, 14, 15, 20, 21]

def is_odd(x):     #sprawdź czy jest parzysta czy nie
    return x % 2 != 0

print(is_odd(7), is_odd(4))

filtered_list = list(filter(is_odd, list_number))  #filter nie zwraca listy, jako pierwszy parametr funkje, jako drugi co ma byc filtrowane
print(filtered_list)

filtered_list = list(filter(lambda x: x % 2 != 0, list_number))
print(filtered_list)

print(list(filter(lambda x: x % 2 != 0, list_number)))


def generate_miltiply_function(n):
    return lambda x: n * x

mul_2 = generate_miltiply_function(2)
mul_3 = generate_miltiply_function(3)

print(mul_2(13),mul_3(8))  #26 (2*13), 24




def mk_thg(a, b, c):
    if c > 0:
        return lambda a, b: a + b
    else:
        return lambda a, b: -a - b


p = mk_thg(1, 2, 1)

print(p(3, 4))