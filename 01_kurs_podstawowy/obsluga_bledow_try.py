import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input("How many persons are there in the team?")
    persons = int(personsStr)

    tasksPerPerson = tasks / persons
except:
    print("Something went wrong...",
          sys.exc_info()[0])  # exec_info zwraca do trzech parametrów, pierwszy to komunikat błędu

print("Every person should have around", tasksPerPerson, "tasks")



# rozszerzenie except
try:
    tasks = 32
    personsStr = input("How many persons are there in the team?")
    persons = int(personsStr)

    tasksPerPerson = tasks / persons
except ValueError as e:  # e dodaje dotatkowe informacje o błędzie
    print("Sorry - you need enter an integer number", e)
except ZeroDivisionError:
    print("Sorry - you need to enter value > 0")
except:
    print("Something went wrong...", sys.exc_info()[0])

print("Every person should have around", tasksPerPerson, "tasks")



# rozszerzenie except i else
try:
    tasks = 32
    personsStr = input("How many persons are there in the team?")
    persons = int(personsStr)

    tasksPerPerson = tasks / persons
except ValueError as e:  # e dodaje dotatkowe informacje o błędzie
    print("Sorry - you need enter an integer number", e)
except ZeroDivisionError:
    print("Sorry - you need to enter value > 0")
except:
    print("Something went wrong...", sys.exc_info()[0])
else:              #wykona się tylko wtedy kiedy nie doszło do żadnego błedu
    print("Every person should have around", tasksPerPerson, "tasks")
finally:           #wykona się tak czy siak
    print("Script finished")
