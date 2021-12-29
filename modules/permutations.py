import math


def n_permute_r(n: int, r: int) -> int:
    """Number of permutations of r items in a set of length n
        nPr == 'n Permute r' == n!/(n-r)!
        Order of items in a permutation matters
        i.e. {ABC} != {BAC}
        """

    if r == n:
        return 1

    if r > n:
        raise ValueError('r must be less than or equal to n')

    return int(math.factorial(n)/math.factorial(n-r))
