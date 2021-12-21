import math
import copy


def n_choose_r(n: int, r: int) -> int:
    """Number of combinations of r items in a set of length n
        nCr == 'n Choose r' == n!/(r!(n-r)!)
        Order of items in a combination doesn't matter
        i.e. {ABC} <==> {BAC}"""

    if r == n:
        return 1

    if r > n:
        raise ValueError('r must be less than or equal to n')

    if n < 0:
        raise ValueError('n must be greater than or equal to zero')

    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def combinations(source: list) -> list:
    """Given a source list of length n, returns the set of all possible combinations
       of length 1 to n (or length 0 for n = 0)"""

    n: int = len(source)

    # n == 0 ✓
    if n == 0:
        return list([])

    # Build a list of n empty lists of n empty lists of n empty lists (i,j,k)
    # (validates those indexes, so they can be iterated over. The alternative
    #  is to append as we go, which requires predetermining the indexes for the iterators)
    # NOTE: r_lists is zero-indexed, while r itself starts at 1
    r_lists: list = [[[] for j in range(0, n)] for i in range(0, n)]

    # The base list is an indexed list of the individual elements from the source list.
    # It will be referenced when building combinations.
    base_list: list = source

    # r == 1
    # Groups of 1, in the built structure, looks like an array of arrays of arrays, with the innermost
    #  array containing just the elements of the source list
    for i in range(0, 1):
        for j in range(i, n):
            for k in range(0, i + 1):
                r_lists[i][j].append([base_list[j]])

    # filter empty lists in the finished r
    r_lists[0] = clean_r_list_i(r_lists[0])

    # r == 2
    # For groups of 2 onward, build recursively using the previous r_lists[i] values

    for i in range(1, n):  # (0 to r - 1 inclusive, i.e. 0 for r == 1) - combinations of i + 1
        for j in range(i, n):  # (0 to n-1 inclusive, i.e. 0 to 2 for n == 3) - this list's nodes
            # build and append this node's elements
            for m in range(i - 1, j):  # (i - 1 to j - 1 inclusive) - the lines from the previous list's nodes
                # we are building and appending new elements to r_lists[i][j], which will be referenced as
                # r_lists[i][j][k]
                # NOTE: these elements are, themselves, lists. E.g. 'abc' is represented as ['a','b','c']

                k_list: list = r_lists[i - 1][m]

                # TODO: see if this filter step is redundant
                # remove any empty elements in k_list
                filter(None, k_list)
                k_concat = copy.deepcopy(k_list)
                for q in range(0, len(k_list)):
                    k_concat[q].append(base_list[j])
                    r_lists[i][j].append(k_concat[q])

    # create a list with index i that consolidates all lists of length i at r_consolidated[i]
    # this is a formatting step for the return object
    r_consolidated: list = [[] for i in range(0, len(r_lists))]
    for i in range(0, len(r_lists)):
        for j in range(0, len(r_lists[i])):
            if r_lists[i][j]:
                for k in range(0, len(r_lists[i][j])):
                    if r_lists[i][j][k]:
                        r_consolidated[i].append(r_lists[i][j][k])

    return r_consolidated


def combinations_r(source: list, r: int) -> list:
    """List of all combinations of length r in a source list of length n"""
    consolidated_combinations: list = combinations(source)

    n: int = len(source)

    # Guards
    if r < 0:
        raise ValueError(f'r ({r}) must be greater than or equal to 0')

    if n < r:
        raise ValueError(f'n ({n}) must be greater than or equal to r ({r})')

    # r == 0 ✓
    if n == 0 or r == 0:
        return list([])

    # consolidated_combinations is zero-indexed, so r --> [r - 1]
    return consolidated_combinations[r - 1]


def clean_r_list_i(r_list_i: list) -> list:
    """remove empty list elements from a list"""
    for j in range(0, len(r_list_i)):
        r_list_i[j] = list(filter(lambda k: k != [], r_list_i[j]))
    return r_list_i


if __name__ == '__main__':
    input_list: list = ['a', 'b', 'c', 'd']
    # input_list: list = ['a', 'b', 'c']
    # input_list: list = ['a', 'b']
    # input_list: list = ['a']
    # input_list: list = []
    print(f'trying {input_list}')
    print(f'combinations(input_list) = {combinations(source=input_list)}')
