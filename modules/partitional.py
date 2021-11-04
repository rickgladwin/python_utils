import copy
from . import bench_timer


class Partitional(list):
    """Extends the list data type. Adds methods for dividing a list into partition sets
       and returning data about those partition sets. A list's partition set for x is the set of
       all possible partitions for the list that will divide the list into x total partitions"""

    # pascals_partitions_statuses
    DEFAULT: int = 0  # set has not been built
    LOCKED: int = 1  # set is being built
    BUILT: int = 2  # set has been built

    def __init__(self, source_list=None):
        super().__init__()
        if source_list is None:
            source_list = []
        self.source_list: list = source_list
        self.n: int = len(source_list)
        self.pascals_partitions: list = [[]]
        self.pascals_partitions_statuses: list = [[]]

        # pascals_partitions is a 2D list (a list of lists)
        # and its elements are sets of lists of lists (a set of lists, each
        # containing one of the possible partition configurations for the source list
        # (a list of lists))

        # NOTE: for this method to be valid, the order of items in source_list has to be
        # arbitrary,
        # because in using pascal's partitions this way (to build the partition set
        # recursively, we assume that m0 can be swapped out with m1, m2, etc. when it
        # comes to position n=1, x=1, and that the labeling, while consistent across
        # all n values, is arbitrary)' (I think?)

        # So there may be another (maybe simpler?) method that applies to source lists
        # where the order is not arbitrary? Or is this method still valid?

        # build a zero-indexed 2D array (n by x) with "empty set" values,
        # with rows n and columns 1..n
        # Used for storing partition sets
        self.pascals_partitions = [[[] for i in range(1, j + 1)] for j in range(1, self.n + 1)]

        # build a zero-indexed 2D array (n by x) with 0 values,
        # with rows n and columns 1..n
        # Used for storing (and coordinating) partition set statuses (prevents collision during memoization)
        self.pascals_partitions_statuses = [[self.DEFAULT for i in range(1, j + 1)] for j in range(1, self.n + 1)]

        # print(f'pascals_partitions init: {self.pascals_partitions}')
        # print(f'pascals_partitions_statuses init: {self.pascals_partitions_statuses}')
        #
        # print(f'constructed Partitional with self.source_list = {self.source_list}')
        # print(f'len(self.source_list) = {len(self.source_list)}')

    # modify the parent functions so that Liskov Substitution is not violated

    ## built-in functions accepting a list instance as an argument
    def __len__(self):
        return len(self.source_list)

    def __enumerate__(self):
        return enumerate(self.source_list)

    ## list object methods
    def append(self, item):
        self.source_list.append(item)
        self.__init__(self.source_list)

    def extend(self, iterable):
        self.source_list.extend(iterable)
        self.__init__(self.source_list)

    def insert(self, position, item):
        self.source_list.insert(position, item)
        self.__init__(self.source_list)

    def remove(self, matched_item):
        self.source_list.remove(matched_item)
        self.__init__(self.source_list)

    def pop(self, *args):
        popped_item = self.source_list.pop(*args)
        self.__init__(self.source_list)
        return popped_item

    def clear(self):
        self.source_list.clear()
        self.__init__(self.source_list)

    def index(self, matched_item, *args):
        return self.source_list.index(matched_item, *args)

    def count(self, matched_item):
        return self.source_list.count(matched_item)

    def sort(self, *, key=None, reverse=False):
        if self.source_list == None:
            return self.source_list
        sorted_list: list = self.source_list.sort(key=key, reverse=reverse)
        self.__init__(self.source_list)
        return sorted_list

    def reverse(self):
        self.source_list.reverse()
        self.__init__(self.source_list)

    def copy(self):
        copied_self = Partitional(self.source_list)
        return copied_self

    def partition_set(self, n: int, x: int) -> list:
        """recursive, memoized function that returns the set of possible partitions for
                self.source_list (or a sublist) with length n and number of partitions x"""

        # print(f'partition_set() called with n = {n}, x = {x}')

        # guards
        # TODO: check that this really is an exception, or simply a case that should return an empty set
        # That is, partition_sets() may be called recursively with values x < 1 or x > n – look at the bounds
        # of Pascal's Triangle for guidance. Yes this guard is valid - don't call this fn
        # if these values are invalid. This fn shouldn't be responsible for validation,
        # only guarding
        # or not? Should this just return an empty set? No, partition_set is never called
        # outside a context of valid n,x values
        if x<1 or x>n:
            raise ValueError(f'number of partitions ({x} given) must be between 1 and n ({n})')

        # base case
        if n == 1 and x == 1:
            base_partition_list: list = []
            base_list: list = [self.source_list[0]]
            base_partition_list.append(base_list)
            self.pascals_partitions[0][0] = [base_partition_list]
            self.pascals_partitions_statuses[0][0] = self.BUILT
            # print(f'--- returning pascals_partitions[0][0] = {self.pascals_partitions[0][0]}')
            return self.pascals_partitions[0][0]

        # recursive cases
        # TODO: is there a potential issue with two threads operating on the same position
        # in pascals_partitions? Either the value is not None but it's not done being
        # constructed, or two threads start appending to that position simultaneously?
        # See if this is possible, and find a fix if so. Might have to pass the memoization
        # variable directly (instead of referencing a class attribute) or give it a status
        # flag (is_filled: bool) that's initialized to False for all positions and is set
        # to True only when `partition_sets` returns for that position.
        # Find out why this isn't an issue with pascal.py - because it's a single value
        # that's either None or an integer? It takes no time to build.
        # Maybe just don't set the value for that position until the return, and check
        # again beforehand?

        # if pascals_partitions status is DEFAULT
        if self.pascals_partitions_statuses[n - 1][x - 1] == self.DEFAULT:
            self.pascals_partitions_statuses[n - 1][x - 1] = self.LOCKED

            # FIXME: extra items (and partition lists?) are being added
            # Works for low n,x – look at cases where x>1 and x<n are BOTH
            # engaged? Is the pascals_partitions element being appended
            # to too many times? Calling for 4,2 breaks. 2,1 returns twice
            # (once correctly, once with extras)

            # look at why low numbers work, and where it breaks. Log more.
            # THERE IT IS. "returning set 2,1" appears twice, the second time
            # with erroneous elements added, so the locks aren't working?

            # build the sets
            # print(f'*** building set with n={n}, x={x}')
            if x>1:
                new_partitions: list = self.__add_partitioned_elements(self.partition_set(n - 1, x - 1), n, x)
                for new_partition in new_partitions:
                    self.pascals_partitions[n - 1][x - 1].append(new_partition)
            if x<n:
                new_partitions: list = self.__add_elements_to_last_partitions(self.partition_set(n - 1, x), n, x)
                for new_partition in new_partitions:
                    self.pascals_partitions[n - 1][x - 1].append(new_partition)

            self.pascals_partitions_statuses[n - 1][x - 1] = self.BUILT
            # return the sets
            # return self.pascals_partitions[n-1][x-1]

        # if pascals_partitions status is LOCKED
        if self.pascals_partitions_statuses[n - 1][x - 1] == self.LOCKED:
            print(f'\nXXX {n},{x} is locked. Waiting.')
            while self.pascals_partitions_statuses[n - 1][x - 1] != self.BUILT:
                continue
            # return the sets
            # return self.pascals_partitions[n - 1][x - 1]

        if self.pascals_partitions_statuses[n - 1][x - 1] == self.BUILT:
            # if n==2 and x==1:
            # print(f'--- returning set {n},{x}: {self.pascals_partitions[n-1][x-1]}')
            return self.pascals_partitions[n - 1][x - 1]
        else:
            raise RecursionError(
                f'partition_sets({n}{x}) ended without pascals_partitions[{n - 1}][{x - 1}] with BUILT status')

    # private
    def __add_partitioned_elements(self, partition_set: list, n: int, x: int) -> list:
        """add a one-element list to each partition list in the set"""
        # print(f'(A) adding to set {partition_set} with n={n}, x={x}')
        new_partition_set = []
        new_partition_list = copy.deepcopy(partition_set)
        for partition_list in new_partition_list:
            # print(f'for partition_list: {partition_list}')
            partition_list.append([self.source_list[n - 1]])
            new_partition_set.append(partition_list)
        # print(f'returning new_partition_set for n={n}, x={x}: {new_partition_set}')
        return new_partition_set

    def __add_elements_to_last_partitions(self, partition_set: list, n: int, x: int) -> list:
        """add one element to the last list in each partition list in the set"""
        # print(f'(B) adding to last partition for set {partition_set} with n={n}, x={x}')
        new_partition_set = []
        new_partition_list = copy.deepcopy(partition_set)
        for partition_list in new_partition_list:
            # print(f'for partition_list: {partition_list}')
            last_partition = partition_list.pop()
            # print(f'last_partition = {last_partition}')
            last_partition.append(self.source_list[n - 1])
            partition_list.append(last_partition)
            new_partition_set.append(partition_list)
        # print(f'returning new_partition_set for n={n}, x={x}: {new_partition_set}')
        return new_partition_set


# print(sys.version)

# TODO: create a utility to generate a set of all groupings of all sizes
#  from a list, if this is not represented with a partitional already.
#  Think about the difference between permutations and combinations?

if (__name__) == "__main__":
    print('initializing array...')
    source_list = [i for i in range(1, 7)]
    partitional = Partitional(source_list)
    p_length = len(partitional)
    p_partitions = 3

    bt = bench_timer.Benchmark()

    bt.start()
    result = partitional.partition_set(p_length, p_partitions)
    bt.end()

    print(f'\npartition set for n={p_length}, x={p_partitions}:')
    # print(f'\n{result}')
    print(f'\nnumber of partition sets: {len(result)}')

    print(f'\n\npartition_sets generated during recursion:\n')
    # for partition_list in result:
    #    print (f'{partition_list}')

    for i in range(1, len(partitional) + 1):
        for j in range(1, i + 1):
            print(f'\n{i},{j}: {partitional.pascals_partitions[i - 1][j - 1]}')
