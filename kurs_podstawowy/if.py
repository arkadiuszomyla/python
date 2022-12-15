age = 18

if age >= 18:
    print("You are adult and you can buy alcohol")
else:
    print("You are too young")

isDrunk = False
isRestrictedArea = True

if age >= 18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("You are too young")

    #if / elif

    if age < 18:
        print("You are adult and you can buy alcohol")
    elif isDrunk:
        print("You are drunk")
    elif isRestrictedArea:
        print("Not here")
    else:
        print("OK, you have Harnaś here")

    #termary operator

    itRains = True

    if itRains:
        print("We stay at home")
    else:
        print("We go out")

    print("We stay at home" if itRains else "We go out")