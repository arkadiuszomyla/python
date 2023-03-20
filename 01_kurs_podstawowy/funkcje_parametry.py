

def GiveWorkingDay(year, month, day):
    # najbliższy dzień roboczy
    from datetime import date
    from datetime import timedelta

    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('Working day for', day, 'is', workingday)
    return

GiveWorkingDay(2099,9,30)
GiveWorkingDay(year=2099,month=9,day=30)
GiveWorkingDay(month=9,day=30,year=2099)


def GiveWorkingDay(year, month, day=1):   #wartosc domyslna parametru, nie trzeba podawać day, albo mozna i nadpisze
    # najbliższy dzień roboczy
    from datetime import date
    from datetime import timedelta

    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('Working day for', day, 'is', workingday)
    return