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

    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))


def list_combinations(source: list) -> list:
    """Given a source list of length n, returns the set of all possible combinations
       of length 1 to n (or length 0 for n = 0)"""

    n: int = len(source)
    s_lists: list = [[[] for j in range(n - i, 0, -1)] for i in range(0, n + 1)]
    r_lists: list = [[] for i in range(0, n + 1)]

    s_lists[0][0] = {'a'}
    s_lists[0][1] = {'b'}
    s_lists[0][2] = {'c'}
    s_lists[0][3] = {'d'}

    s_lists[1][0] = {'ab', 'ac', 'ad'}
    s_lists[1][1] = {'bc', 'bd'}
    s_lists[1][2] = {'cd'}

    # s_lists[2][0] = {'abc', 'abd'}

    print(f'r_lists = {r_lists}')
    print(f's_lists = {s_lists}')

    if n == 0:
        print(f'returning {list([])}')
        return list([])

    if n == 1:
        print(f'returning {source}')
        return source

    # init
    # r = 0 --> combinations of length 0 (one combination, an empty list)
    r_lists[0] = [[]]
    print(f'r_lists[0] = {r_lists[0]}')

    # r = 1 --> combinations of length 1 (n combinations, each element in source)
    for i in range(0, n):
        r_lists[1].append(list(source[i]))

    print(f'r_lists[1] = {r_lists[1]}')

    for i in range(2, n + 1):
        print(f'\n----------------------\n')
        last_list: list = r_lists[i - 1]
        print(f'last_list (r_lists[{i - 1}]): {last_list}')
        this_list: list = r_lists[i]
        print(f'this_list (r_lists[{i}]): {this_list}')
        last_list_length: int = len(last_list)

        for j in range(0, last_list_length):
            # for j in range(0, i):
            # print(f'j = {j} of {last_list_length - 1}')
            # print(f'j = {j} of {i - 1}')
            # base_combo = list(last_list[j])
            # print(f'appending to base combo: {base_combo}')

            for k in range(j + 1, n):
                base_combo = list(last_list[j])
                print(f'appending to base combo (last_list[j]): {base_combo}')
                print(f'i = {i} of {n}')
                print(f'j = {j} of {i-1}')
                print(f'k = {k} of {n-1}')
                print(f'source[k] = {source[k]}')
                base_combo.append(source[k])
                this_list.append(base_combo)
                print(f'this_list (r_lists[{i}]) = {this_list}')

    print(f'list_combinations returns r_lists: {r_lists}')

    return r_lists


if __name__ == '__main__':
    input_list: list = ['a', 'b', 'c', 'd']
    # input_list: list = ['a', 'b', 'c']
    # input_list: list = ['a', 'b']
    # input_list: list = ['a']
    # input_list: list = []
    print(f'trying {input_list}')
    list_combinations(source=input_list)
