import itertools as it

def pan(n=10):
    '''generates n-digit pandigital numbers'''
    for i in (int(''.join(map(str,x))) for x in it.permutations(range(1,n+1))):
        yield i

def isPan(x, n=10, zeroless=True):
    ''' checks if x is an n-digit pandigital number '''
    x = ''.join(sorted(str(x))).lower()
    target = '0123456789'
    return x == target[zeroless:n+int(not zeroless)]
