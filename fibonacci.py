from math import sqrt

def fib():
    ''' Generates fibonacci number '''
    a, b = (0, 1)
    while True:
        yield a
        a, b = b, a + b

def isFib(n):
    ''' Checks if n is a fibonacci number '''
    phi = 0.5 + 0.5 * sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n
