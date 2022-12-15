#date and time
import datetime

print("Minimum and maximum", datetime.MINYEAR, datetime.MAXYEAR)


#różnice czasu od obecnego
d1 = datetime.timedelta(days=1, hours=2, minutes=30)
print(d1)

d2 = datetime.timedelta(days=-1, hours=-2, minutes=-3)
print(d2)


print("Today is", datetime.date.today())
today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print(daysToPay)
print("Today is", today)
print("Bills should be paid till", today+daysToPay)


endOfTheWorld = datetime.date.max
print("The final end of the world will happen by Python:", endOfTheWorld)
print(endOfTheWorld.weekday())

bornDate = datetime.date(1989, 8, 7)
today = datetime.date.today()
print(today - bornDate)   #ilość dni życia

print('Now()\t', datetime.datetime.now()) #zwraca date i godzine
print("today()\t", datetime.datetime.today())
print("utcnow()\t", datetime.datetime.utcnow())   #uniwersalny czas
print("weekdat()\t", datetime.datetime.today().weekday())

print("%a", datetime.datetime.now.strptime("%a")) #zwraca date w określonym formacie (dzień, skrócony dzień, itp itd)
print("%A", datetime.datetime.now.strptime("%A"))
print("%w", datetime.datetime.now.strptime("%w"))
print("%a %A %w", datetime.datetime.now.strptime("%a %A %w"))
print("%Y-%m-%d_%h_%M_%S_%f",\
      datetime.datetime.now().strptime("%Y-%m-%d_%h_%M_%S_%f"))