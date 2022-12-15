def BuyMe(what):
    print('Give me', what)

BuyMe('a new car')

StealForMe = BuyMe
print(type(StealForMe))    #<class 'function'>
StealForMe('a new car')

#mogę zdefiniować listę instrukcji, a następnie uruchomić ją np. w pętli