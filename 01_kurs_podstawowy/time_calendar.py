import time
# sprawdzenie wersji pythona
import sys

print(sys.version)
# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))

# czas
print("Current time is... inix epoch", time.time()) #zwraca czas w sposób unixowy
print("\n")
print("Current time is... tuple", time.localtime(time.time())) #zwraca tuple z aktualnym czasem
print("Current tine is.. for human", time.asctime(time.localtime(time.time())))
#print("Current tine is... for human", time.localtime(time.clock()))

#kalendarz
import calendar
print(calendar.month(2017, 9, w=5, l=2))   #wyświetla kalendarz, okno w danym rozmiarze
print(calendar.month(2017,9))              #wyświela kalendarz
print("week day is", calendar.weekday(2017,9,29)) #który to dzień tygodnia
calendar.setfirstweekday(6)  #ustawia pierwszy dzień tygodnia
print(calendar.month(2017,9)) #kalendarz gdzie pierwszy dzien tygodnia to wyzej
print("week day is", calendar.weekday(2017,9,29)) # nie zmienia

print("Is 2020 a leap year?", calendar.isleap(2020))  #rok przestępny

print("Leap days 2000-2017", calendar.leapdays(2000, 2017))  #ile było dni przestępnych
print(calendar.calendar(2018)) #wyświetla kalendarz na cały rok