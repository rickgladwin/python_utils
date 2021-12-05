import math


def n_choose_r(n: int, r: int) -> int:
    """Number of combinations of r items in a set of length n
        nCr == 'n Choose r' == n!/(r!(n-r)!)
        Order of items in a combination doesn't matter
        i.e. {ABC} <==> {BAC}
        """

    if r == n:
        return 1

    if r > n:
        raise ValueError('r must be less than or equal to n')

    if n < 0:
        raise ValueError('n must be greater than or equal to zero')

    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def list_combinations(source: list) -> list:
    """Given a source list of length n, returns the set of all possible combinations
       of length 1 to n (or length 0 for n = 0)"""

    n: int = len(source)
    s_lists: list = [[None for j in range(0, n)] for i in range(0, n)]
    r_lists: list = [[] for i in range(0, n + 1)]

    print(f'init r_lists = {r_lists}')
    print(f'init s_lists = {s_lists}')
    print(f'')
    #
    # print(f's_lists[2][1]: {s_lists[2][1]}')

    # expected output from input ['a', 'b', 'c', 'd']
    # where s_lists[i][j][k] ==> s_lists[r - 1][j][k]
    s_lists[0][0] = [['a']]
    s_lists[0][1] = [['b']]
    s_lists[0][2] = [['c']]
    s_lists[0][3] = [['d']]

    s_lists[1][1] = [['a', 'b']]
    s_lists[1][2] = [['a', 'c'], ['b', 'c']]
    s_lists[1][3] = [['a', 'd'], ['b', 'd'], ['c', 'd']]

    s_lists[2][2] = [['a', 'b', 'c']]
    s_lists[2][3] = [['a', 'b', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd']]

    s_lists[3][3] = [['a', 'b', 'c', 'd']]

    # print(f'r_lists = {r_lists}')
    print(f's_lists = {s_lists}')

    print(f's_lists[2][1]: {s_lists[2][1]}')

    if n == 0:
        print(f'returning {list([])}')
        return list([])

    # init
    # r = 0 --> combinations of length 0 (one combination, an empty list)
    r_lists[0] = [[]]
    print(f'r_lists[0] = {r_lists[0]}')

    # r = 1 --> combinations of length 1 (n combinations, each element in source)
    for i in range(0, n):
        r_lists[1].append(list(source[i]))

    if n == 1:
        print(f'returning r_lists[1]: {r_lists[1]}')
        return r_lists[1]

    print(f'r_lists[1] = {r_lists[1]}')

    print(f'list_combinations returns r_lists: {r_lists}')

    # n == 2:
    # for i in range()

    # base list = B = source
    # B[0] = source[0], B[1] = source[1], etc.

    # all combinations of length r is the list R[r] = concatenation of S[j]
    # where

    return r_lists


def combinations_r(source: list, r: int) -> list:
    """List of all combinations of length r in a source list of length n"""
    n: int = len(source)

    if r < 0 or n < 0:
        raise ValueError(f'n ({n}) and r ({r}) must be greater or equal to 0')

    if n < r:
        raise ValueError(f'n ({n}) must be greater than or equal to r ({r})')

    if n == 0 or r == 0:
        return list([])

    base_list: list = source
    r_lists: list = [[] for i in range(0, n)]

    if r == 1:
        for i in range(0, n):
            r_lists[i] = list(base_list[i])
        return r_lists


if __name__ == '__main__':
    input_list: list = ['a', 'b', 'c', 'd']
    # input_list: list = ['a', 'b', 'c']
    # input_list: list = ['a', 'b']
    # input_list: list = ['a']
    # input_list: list = []
    print(f'trying {input_list}')
    list_combinations(source=input_list)
