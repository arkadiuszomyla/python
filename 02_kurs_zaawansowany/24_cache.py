import time
import functools

@functools.lru_cache()      #python będzie zapamiętywał wyniki już wykonanych obliczeń, funkcja musi być deterministyczna, musi za każdym razem zwracać ten sam wynik
def Factorial(n):      #silnia
    time.sleep(0.1)     #jedna dziesiąta sekundy
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)

start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Execution time', stop - start)

print(Factorial.cache_info())   #zwraca informacje ile wyników zapamiętał