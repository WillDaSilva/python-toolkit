from math import floor, sqrt
import itertools as it

def prime():
    ''' Generates prime numbers '''
    D = {9:3,25:5}
    yield 2
    yield 3
    yield 5
    MASK= 1,0,1,1,0,1,1,0,1,0,0,1,1,0,0
    MODULOS= frozenset((1,7,11,13,17,19,23,29))
    for q in it.compress(it.islice(it.count(7),0,None,2),it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q**2] = q
            yield q
        else:
            x = q + 2 * p
            while (x % 30) not in MODULOS or x in D:
                x += 2 * p
            D[x] = p

def isPrime(n):
    ''' Checks if n is a prime number'''
    return n > 1 and all(n%i for i in it.islice(it.count(2), int(sqrt(n)-1)))

def _primeOrder(n, p):
    ''' The order of a prime number p for n '''
    order = 0
    while not n % p:
        n = n // p
        order += 1
    return order

def _primeFactorInner(n, start):
    ''' Inner function for primeFactor() '''
    if n < start: return
    for p in it.takewhile(lambda x: x < floor(sqrt(n)) + 1, prime()):
        a = _primeOrder(n, p)
        if (a > 0):
            yield (p, a)
            n = n // (p ** a)
            if n == 1:
                return
    if n > 1:
        yield (n, 1)

def primeFactor(n, flat=False, unique=False):
    '''
    Generates prime factors of n

    Generates tuples of the form (prime, order)

    If flat is True, generates primes instead of tuples.

    If unique is True, generates each prime once regardless of its order.
    unique does nothing if flat is not True.
    '''
    p = _primeFactorInner(n, 2)
    if flat:
        if unique:
            for i in (x for x, y in p):
                yield i
        for i in (it.repeat(x, y) for x, y in p):
            yield from i
    yield from p
