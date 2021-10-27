import math

# nPr
# "n permute r"
# Permutations: number of arrangements of r items from n objects
# Order matters (see combinations), i.e. [a,b] != [b,a]
# nPr = n!/(n-r)!
def permute(n: int, r: int):
    if r == n:
        return 1
    if r > n:
        raise ValueError('r must be less than or equal to n')
    nPr = math.factorial(n)/math.factorial(n-r)
    return nPr


def permutations(items: list, r: int) -> set:
    # 
    return {None}