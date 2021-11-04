import math


def n_choose_r(n: int, r: int) -> int:
    """Number of combinations of r items in a set of length n
       nCr == 'n Choose r' == n!/(r!(n-r)!)
       order of items in a combination doesn't matter
       i.e. {ABC} == {BAC}"""

    if r > n:
        raise ValueError('r must be less than or equal to n')

    if n < 0:
        raise ValueError('n must be greater than or equal to zero')

    return int(math.factorial(n)/(math.factorial(r) * math.factorial(n-r)))


def combinations(source: set) -> set:
    """Given a source set of length n, returns the set of all possible combinations
       of length 1 to n (or length 0 for n = 0)"""

    return set(source)
