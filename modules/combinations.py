import math
import copy


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

    # Guards
    if r < 0 or n < 0:
        raise ValueError(f'n ({n}) and r ({r}) must be greater than or equal to 0')

    if n < r:
        raise ValueError(f'n ({n}) must be greater than or equal to r ({r})')

    # r == 0 ✓
    if n == 0 or r == 0:
        return list([])

    # Build a list of n empty lists of n empty lists of n empty lists (i,j,k)
    # NOTE: r_lists is zero-indexed, while r itself starts at 1
    r_lists: list = [[[[] for k in range(0, n)] for j in range(0, n)] for i in range(0, n)]
    print(f'r_lists init: {r_lists}')

    # The base list is an indexed list of the individual elements from the source list.
    # It will be referenced when building combinations.
    base_list: list = source
    print(f'base_list: {base_list}')
    print(f'r_lists: {r_lists}')
    print(f'r_lists[0]: {r_lists[0]}')
    print(f'r_lists[0][0]: {r_lists[0][0]}')
    print(f'r_lists[0][0][0]: {r_lists[0][0][0]}')

    # for i in range(0, r):
    #     for j in range (r-1,)
    #     r_lists[i] = list(base_list[i])

    # r == 1
    # Groups of 1, in the built structure, looks like an array of arrays of arrays, with the innermost
    #  array containing just the elements of the source list
    for i in range(0, 1):
        for j in range(i, n):
            for k in range(0, i + 1):
                print(f'i, j, k: {i}, {j}, {k}')
                print(f'-- base_list[{j}] = {base_list[j]}')
                r_lists[i][j][k] = base_list[j]
                print(f'------ r_lists[{i}][{j}][{k}] = {r_lists[i][j][k]}')

    print(f'----- done r == 1')
    print(f'----- r_lists: {r_lists}')

    # r == 2
    # For groups of 2 onward, build recursively using the previous r_lists[i] values

    for i in range(1, 2):  # (0 to r - 1 inclusive, i.e. 0 for r == 1) - combinations of i + 1
        for j in range(i, n):  # (0 to n-1 inclusive, i.e. 0 to 2 for n == 3) - this list's nodes
            for m in range(i - 1, j):  # (i - 1 to j - 1 inclusive) - the lines from the previous list's nodes
                print(f'i: {i}, j: {j}, m: {m}')

                # we are building and appending new elements to r_lists[i][j], which will be referenced as
                # r_lists[i][j][k]

                # TODO: write this part of the algorithm
                # for each element k in i - 1, j??, m?? (previous i list nodes)
                #  append base_list[j] to r_lists[i - 1][m][k]
                #  push the result to r_lists[i][j] (as r_lists[i][j][k])

    #             print(f'r_lists_previous: {r_lists_previous}')
    #             print(f'base_list[j]: {base_list[j]}')
    #             print(f'append: {r_lists_previous.append(base_list[j])}')
    #             print(f'appended: {r_lists_previous}')
    #             print(f'r_lists[i][j] before: {r_lists[i][j]}')
    #             r_lists[i][j].append(r_lists_previous)
    #             print(f'r_lists[i][j] after: {r_lists[i][j]}')

                # print(f'r_lists[i][j] before: {r_lists[i][j]}')
                # r_lists[i][j].append(list(base_list[j]))  # [[base_list[0]], [base_list[1]], [base_list[2]]
                # print(f'r_lists[i][j] after: {r_lists[i][j]}')

    # print(f'\n--------------- r_lists[0] -----------------')
    # print(f'after r == 1: {r_lists[0]}')
    # print(f'r_lists[0][0][0]: {r_lists[0][0][0]}')

    # r == 2
    # for i in range(1, 2):  # (1 to r - 1 inclusive, i.e. 1 for r == 2)
    #     print(f'\n--------------- r_lists[{i}] -----------------')
    #     for j in range(i, n):  # (1 to n-1 inclusive, i.e. 1 to 2 for n == 3)
    #         for k in range(1, j + 1):  # (k is not used as a list index directly, hence 1 to j + 1)
    #             print(f'i: {i}, j: {j}, k: {k}')
    #             r_lists_previous: list = copy.deepcopy(r_lists[i - 1][j - k])
    #             print(f'r_lists_previous: {r_lists_previous}')
    #             print(f'base_list[j]: {base_list[j]}')
    #             print(f'append: {r_lists_previous.append(base_list[j])}')
    #             print(f'appended: {r_lists_previous}')
    #             print(f'r_lists[i][j] before: {r_lists[i][j]}')
    #             r_lists[i][j].append(r_lists_previous)
    #             print(f'r_lists[i][j] after: {r_lists[i][j]}')
    #
    # for i in range(0, n):
    #     print(f'\nr_lists[{i}]: {r_lists[i]}')

    # consolidate all combinations in i
    # TODO: range from 0 to n
    r_consolidated: list = [[] for i in range(0, 1)]
    for i in range(0, n):
        for j in range(0, len(r_lists[i])):
            if r_lists[i][j]:
                for k in range(0, len(r_lists[i][j])):
                    if r_lists[i][j][k]:
                        r_consolidated[i].append([r_lists[i][j][k]])

    print(f'------------- r_consolidated: {r_consolidated}')
    # r_lists is zero-indexed, so r --> [r - 1]
    return r_consolidated[r - 1]


if __name__ == '__main__':
    input_list: list = ['a', 'b', 'c', 'd']
    # input_list: list = ['a', 'b', 'c']
    # input_list: list = ['a', 'b']
    # input_list: list = ['a']
    # input_list: list = []
    print(f'trying {input_list}')
    list_combinations(source=input_list)
