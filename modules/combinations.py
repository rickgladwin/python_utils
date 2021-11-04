import math

# nCr
# "n choose r"
# Combinations: number of collections of r items from n objects
# Order doesn't matter (see permutations), i.e. [a,b] <==> [b,a]
# nCr = n!/r!(n-r)!
def choose(n: int, r: int):
    if r == n:
        return 1
    if r > n:
        raise ValueError('r must be less than or equal to n')
    nCr = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    return nCr


def combinations(items: list, r: int, all_combinations=None) -> set:
    # combinations of length r in list of length n
    if all_combinations is None:
        all_combinations = {}
    if r == 1:
        return set(list)
    else:
        # add an element of items to each element in combinations(list, r-1)

    return {None}

def build_combo_set(all_sets, combo_length: int) -> list:
    if combo_length == 1:
        return all_sets[0]

    set_one_smaller = all_sets[combo_length-1]
    combo_length_list = []
    for combo in set_one_smaller:
        for combo_length_1 in all_sets[0]:
            # TODO: map this out
    all_sets.append(combo_length_list)
    return all_sets

