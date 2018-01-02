from math import sqrt

def polygonal(s, n):
    ''' The n-th s-gonal number '''
    assert s > 2 and isinstance(s, int) and isinstance(n, int)
    return (n**2 * (s - 2) - (n * (s - 4))) // 2

def isPolygonal(s, n):
    ''' Check if n is a s-gonal number '''
    assert s > 2 and s % 1 == 0 and n % 1 == 0
    x = (sqrt(8 * (s - 2) * n + (s - 4) ** 2) + (s - 4)) / (2 * (s - 2))
    return x % 1 == 0
