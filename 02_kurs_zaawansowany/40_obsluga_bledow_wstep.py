clients = {
    "INFO": 0.5,
    "DATA": 0.2,
    "SOFT": 0.2,
    "INTER": 0.1,
    "OMEGA": 0.0
}

myClient = input("Enter client's name: ")
totalCost = 7200


try:
    print('The % ratio for {} is {}'.format(myClient, clients[myClient]))
except:
    print('Sorry we have an error..')
else:
    print('The cost for {}'.format(myClient, clients[myClient] * totalCost))
finally:
    print('-= Calculation finished =-')


try:
    print('The % ratio for {} is {}'.format(myClient, clients[myClient]))
except Exception as e:
    print('Sorry we have an error..\nDetails:\n{}'.format(e))
else:
    print('The cost for {}'.format(myClient, clients[myClient] * totalCost))
finally:
    print('-= Calculation finished =-')
