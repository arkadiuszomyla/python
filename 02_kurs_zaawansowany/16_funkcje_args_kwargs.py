def buyMe(prefix = 'Please buy me', what = 'something nice', *args):    #pozwala wprowadzać dowolną liczbę parametrów, tuplet
    print(prefix, what)
    print(args)

buyMe('Please buy me', 'a new car', 'a cat', 'a dog', 'a dragon')



def buyMe(prefix = 'Please buy me', what = 'something nice', **kwargs):    #pozwala wprowadzać dowolną liczbę parametrów, poprzedzając je słowem kluczowym, słowik
    print(prefix, what)
    print(kwargs)

buyMe('Please buy me', 'a new car', shop='market', color='any')

products = ['milk','bread']
parameters = {'price':'low', 'time':'now'}


def buyMe(prefix = 'Please buy me', what = 'something nice', *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)

buyMe('Please buy me', 'a new car', *products, **parameters)