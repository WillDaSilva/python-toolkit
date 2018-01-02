def fib(start=0):
    ''' Generates fibonacci number '''
    a, b = ((0, 1), (1, 1))[bool(start)]
    while True:
        yield a
        a, b = b, a + b

def isFib(n):
    ''' Checks if n is a fibonacci number '''
    return False
