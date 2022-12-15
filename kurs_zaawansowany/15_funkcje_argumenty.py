def buyMe(prefix, what):
    print(prefix, what)


buyMe('Please buy me', 'a new car')
buyMe(prefix = 'Please buy me', what = 'a new car')
buyMe(what = 'Please buy me', prefix = 'a new car')


def buyMe(prefix, what = 'something nice'):
    print(prefix, what)

buyMe(prefix = 'Please buy me')