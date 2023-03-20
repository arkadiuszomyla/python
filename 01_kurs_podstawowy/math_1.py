f_smaller = 3.14159265335895389
f_bigger = 3.87756392764

print(f_smaller, f_bigger)
print("\n")
print(int(f_smaller), int(f_bigger))
print("\n")
print(abs(f_smaller, abs(-f_smaller)))
print("\n")
print(round(f_smaller, 2), round(f_bigger), round(f_bigger, 3))
print("\n")
print(min(f_smaller, f_bigger), max(f_smaller, f_bigger))   # wyciąga wartość najmniejszą, największą
print("\n")

list=[1,2,3,4,5,6,3,2,1]
print(sum(list), len(list))  #suma elementów, ile elementów
print("\n")
print(sum(list)/len(list))  #średnia

print(round(2.654, 2))  #float źle zaokrągla



#import math
from math import *
#from math import pi

#print(math.pi)
print(pi)

percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
           2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
           3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
           4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
           8.740978348, 6.174819567]

percent.sort()
print(percent)

# this ends with error
# print(median(percent))
# print(median_low(percent))
# print(median_high(percent))
# this succeeds
import statistics

print(statistics.median(percent))
print(statistics.median_low(percent))
print(statistics.median_high(percent))

# this succeedes
from statistics import *

print(median(percent))
print(median_low(percent))
print(median_high(percent))