def WeekDayInFrench(dayNumber):
    names = {
        0: "lundi",
        1: "mardi",
        2: "mercedi",
        3: "jeudi",
        4: "vendredi",
        5: "samedi",
        6: "dimanche"
    }

    return names.get(dayNumber, "error")

print(WeekDayInFrench(1))