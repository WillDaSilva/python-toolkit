from .misc import product
import itertools as it
from math import factorial

def nPr(n, r):
    ''' Number of ordered permutations of r items taken from a population of size n '''
    assert 0 <= r <= n
    return product(range(n + 1 - r, n + 1))

def nCr(n, r):
    ''' Number of unordered combinations of r items from a population of size n '''
    assert 0 <= r <= n
    return nPr(n, r) // factorial(r)

def compositions(n, width):
    ''' Weak compositions of n '''
    for c in it.combinations(range(n + width - 1), width - 1):
        z = zip(it.chain((-1,), c), it.chain(c + (n + width - 1,)))
        yield tuple(y - x - 1 for x, y in z)
