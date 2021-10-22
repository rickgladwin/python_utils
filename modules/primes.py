import math
import bench_timer


class Primes:
    """contains methods for working with prime numbers"""

    # reference primes: [
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    # 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
    # 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
    # 167, 173, 179, 181, 191, 193, 197, 199
    # ]
    sample_primes = []

    def prime_numbers(self, upper_bound: int) -> list:
        """Uses Sieve of Eratosthenes to generate a list of prime numbers from 2 to an upper bound"""

        self.sample_primes = []

        # initialize a primes map with length upper_bound + 1
        # to accommodate the zero index
        primes_map = [True] * (upper_bound + 1)

        # make non-prime values in the primes map false
        # if they are a multiple of smaller values
        for i in range(2, upper_bound):
            if primes_map[i]:
                for j in range(2, int(upper_bound/i) + 1):
                    if i * j < len(primes_map):
                        primes_map[i * j] = False

        # use the primes map to generate a list of primes
        for k in range(2, upper_bound + 1):
            if primes_map[k]:
                self.sample_primes.append(k)

        return self.sample_primes

    def nth_prime_number(self, n: int) -> int:
        """Uses the Prime Number Theorem to choose a range, then uses Sieve of Eratosthenes to generate
        a list of prime numbers with index 0 to n-1, and returns the nth prime"""

        if n == 1:
            return 2

        self.sample_primes = []

        # π(x) ~ x/ln x, where x is a prime number x and π(x) is the count of prime numbers up to x
        # As a consequence of this, p(n) ~ n ln n, where p(n) is the nth prime number
        # So we can set our upper bound above n ln n

        # TODO: a more precise numerical result for this upper bound will make this function more efficient
        # the equation used here guarantees a valid range for n < 1000, but the difference between
        # the upper bound and p(n) varies.
        upper_bound = int(n*math.log(n)) + 2*n

        # nth_prime = self.prime_numbers(upper_bound)[n-1]
        # print(f'difference: {upper_bound - nth_prime}')

        # generate list of primes and return the nth prime
        return self.prime_numbers(upper_bound)[n-1]

    def is_prime(self, test_number: int) -> bool:
        """Uses successive division by primes up to sqrt(n) to determine if n is prime"""

        if test_number in [0, 1]:
            return False

        # check if test_number has already been determined to be prime
        if test_number in self.sample_primes:
            return True

        test_sqrt = int(math.sqrt(test_number))
        self.generate_primes_as_needed(upper_bound=test_sqrt)

        test_denominator = 2
        index = 0
        while test_denominator <= test_sqrt and index < len(self.sample_primes):
            test_denominator = self.sample_primes[index]
            if test_number % test_denominator == 0:
                return False
            index += 1
        return True

    def get_prime_factors_set(self, n: int) -> set:
        """Gets a set (unique values) of prime factors of n after ensuring sample primes are present"""
        test_sqrt = int(math.sqrt(n))
        self.generate_primes_as_needed(upper_bound=test_sqrt)
        return self.prime_factors_set(n)

    def prime_factors_set(self, n: int, found=None) -> set:
        """recursive, memoized function to find a set of prime factors"""
        if found is None:
            found = set()
        if self.is_prime(test_number=n):
            found.add(n)
            return found
        for sample_prime in self.sample_primes:
            if n % sample_prime == 0:
                found.add(sample_prime)
                return self.prime_factors_set(int(n / sample_prime), found)
        return found

    def get_prime_factors_list(self, n: int) -> list:
        """Gets a list (repeat values allowed) of prime factors of n after ensuring sample primes are present"""
        test_sqrt = int(math.sqrt(n))
        self.generate_primes_as_needed(upper_bound=test_sqrt)
        return self.prime_factors_list(n)

    def prime_factors_list(self, n: int, found=None) -> list:
        """recursive, memoized function to find a list of prime factors"""
        if found is None:
            found = []
        if self.is_prime(test_number=n):
            found.append(n)
            return found
        for sample_prime in self.sample_primes:
            if n % sample_prime == 0:
                found.append(sample_prime)
                return self.prime_factors_list(int(n / sample_prime), found)
        return found

    def generate_primes_as_needed(self, upper_bound: int) -> None:
        """Ensures there are sufficient primes in the sample list"""
        if len(self.sample_primes) > 0 and self.sample_primes[-1] < upper_bound or len(self.sample_primes) == 0:
            self.prime_numbers(upper_bound=upper_bound)

    def largest_prime_factor(self, n: int) -> int:
        """Returns the largest prime factor of n"""
        found_prime_factors = self.get_prime_factors_set(n)
        if len(found_prime_factors) == 0:
            return n
        else:
            return max(found_prime_factors)


primes = Primes()
benchmark = bench_timer.Benchmark()

# benchmark.start()
# print(primes.prime_numbers(upper_bound=4000000)[-1])
# print(primes.prime_numbers(upper_bound=400))
# for j_test in range(24, 47):
#     print(f'test: {j_test}, is prime: {primes.is_prime(j_test)}')
# benchmark.end()

# benchmark.start()
# test_n = 456
# prime_factors = primes.get_prime_factors_list(test_n)
# print(f'prime factors (list) of {test_n}: {prime_factors}')
# print(f'largest prime factor: {primes.largest_prime_factor(test_n)}')
# benchmark.end()

# benchmark.start()
# for i in range(1, 1000):
#     print(f'{i}th prime: {primes.nth_prime_number(i)}')
# benchmark.end()

benchmark.start()
j_test = 10001
print(f'{j_test}th prime: {primes.nth_prime_number(j_test)}')
benchmark.end()
