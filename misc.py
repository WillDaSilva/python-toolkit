from math import factorial, sqrt, gcd
from operator import mul
import heapq
from functools import reduce
from collections import Iterable, Iterator, deque
import itertools as it
from .prime import primeFactor

def product(iterable):
    ''' The product of the items in n '''
    return reduce(mul, iterable)

def nPr(n, r):
    ''' The number of ordered permutations of r items taken from a population of size n '''
    assert 0 <= r <= n
    return product(range(n + 1 - r, n + 1))

def nCr(n, r):
    ''' The number of unordered combinations of r items from a population of size n '''
    assert 0 <= r <= n
    return nPr(n, r) // factorial(r)

def lcm(a, b):
    return a * b // gcd(a, b)

def factor(n):
    primes = [(1, 1)] + list(primeFactor(n))
    q = [(1, 0, 1)]
    while len(q) > 0:
        # d is the divisor
        # i is the index of its largest "prime" in primes
        # a is the exponent of that "prime"
        (d, i, a) = heapq.heappop(q)
        yield d
        if a < primes[i][1]:
            heapq.heappush(q, (d * primes[i][0], i, a + 1))
        if i + 1 < len(primes):
            heapq.heappush(q, (d * primes[i + 1][0], i + 1, 1))
            # The condition i > 0 is to avoid duplicates arising because
            # d == d // primes[0][0]
            if i > 0 and a == 1:
                heapq.heappush(q, (d // primes[i][0] * primes[i + 1][0], i + 1, 1))


# def factor(n):
#     primes, ranges = zip(*primeFactor(n))
#     z = it.product(*(range(x + 1) for x in ranges))
#     yield from (product(a ** b for a, b in zip(primes, q)) for q in z)

def numFactor(n):
    ''' The number of factors of n '''
    if n in (0, 1):
        return n or None
    elif n < 0:
        return product((x[1] + 1 for x in primeFactor(-n))) + 1
    return product((x[1] + 1 for x in primeFactor(n)))

def flatten(x, depth=None, ignore=None, types=None):
    '''
    Generates a flat representation of an iterable

    Completely flattens if depth is None
    Otherwise, flattens depth layers

    Does not flatten types specified by the tuple ignore
    If types is specified, only flattens types specified by the tuple types
    '''
    ignore = tuple(ignore or ())
    ignore += (str, bytes) # flattening a string results in RecursionError
    recurse = depth is None or depth
    for i in x:
        if isinstance(i, Iterable) and not isinstance(i, ignore) and recurse:
            depth = depth and depth - 1
            if types:
                if isinstance(i, types):
                    yield from flatten(i, depth, ignore, types)
                else:
                    yield i
            else:
                yield from flatten(i, depth, ignore, types)
        else:
            yield i

def tail(n, iterable):
    ''' Iterator over the last n items from iterable '''
    return iter(deque(iterable, maxlen=n))

def consume(iterator, n=None):
    ''' Advance the iterator n-steps ahead. If n is none, consume entirely. '''
    if n is None:
        deque(iterator, maxlen=0)
    else:
        next(it.islice(iterator, n, n), None)

def nth(iterable, n, default=None):
    ''' Returns the nth item or a default value '''
    return next(it.islice(iterable, n, None), default)

def pairwise(iterable):
    '''
    Generates

    pairwise(iterable) --> (s0, s1), (s1, s2), (s2, s3), ...
    '''
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)

def grouper(iterable, n, fillvalue=None):
    '''
    Generates fixed-length chunks from iterable

    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    '''
    args = [iter(iterable)] * n
    return it.zip_longest(*args, fillvalue=fillvalue)

def roundrobin(*iterables):
    '''
    Generates entries from each iterables in turn.
    Yields elements until the largest iterable is exausted.

    roundrobin('ABC', 'D', 'EF') --> A D E B F C
    '''
    pending = len(iterables)
    nexts = it.cycle(iter(i).__next__ for i in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = it.cycle(it.islice(nexts, pending))

def partition(pred, iterable):
    ''' Partitions iterable into false entries and true entries '''
    t1, t2 = tee(iterable)
    return it.filterfalse(pred, t1), filter(pred, t2)

def powerset(x):
    ''' The powerset of x '''
    s = list(x)
    return list(flatten((it.combinations(s, r) for r in range(len(s) + 1)), 1))

def unique_everseen(iterable, key=None):
    '''
    Yields unique elements from iterable

    unique_everseen('AAAABBBCCDAABBB') --> A B C D
    unique_everseen('ABBCcAD', str.lower) --> A B C D
    '''
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

def unique_justseen(iterable, key=None):
    '''
    Yields elements from iterable which are not equal their previous element

    unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    unique_justseen('ABBCcAD', str.lower) --> A B C A D
    '''
    return map(next, map(itemgetter(1), groupby(iterable, key)))

def first_true(iterable, pred=None, default=None):
    '''
    The first true value in the iterable.

    If no true value is found, returns default

    If pred is not None, returns the first item for which pred(item) is true.

    first_true([a,b,c], x) --> a or b or c or x
    first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
    '''
    return next(filter(pred, iterable), default)

def digitize(n, reverse=True):
    '''
    Yields digits from n

    By default, yields digits in reverse order
    Set reverse parameter to False to obtain digits in the correct order.
    Yielding digits in forwards order decreases preformance.
    '''
    if not reverse:
        digits = []
    while n:
        n, x = divmod(n, 10)
        if reverse:
            yield x
        else:
            digits.append(x)
    if not reverse:
        yield from reversed(digits)

def isPalindrome(n):
    n = str(n)
    return all(n[x] == n[-(x + 1)] for x in range(len(n)//2 + 1))

def reverseInt(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r

