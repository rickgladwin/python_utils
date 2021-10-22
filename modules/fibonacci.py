import math
import bench_timer


class Fibonacci:
    """Contains methods for generating and working with Fibonacci numbers"""

    fibs = [1, 1]

    def fib(self, n: int) -> int:
        """recursive memoized function to retrieve fibonacci number
            at position n in the set of all Fibonacci numbers fibs[0]..fibs[n]
            while generating a set of all Fibonacci numbers up to fibs[n]"""
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n < len(self.fibs) and self.fibs[n]:
            return self.fibs[n]
        else:
            self.fibs.insert(n, self.fib(n-1) + self.fib(n-2))
            return self.fibs[n]

    def fib_in_constant_space(self, n:int) -> int:
        """returns the nth (0-indexed) Fibonacci number F(n) using O(1) space
            and discards all other Fibonacci numbers up to F(n) except for
            values in the 'one back' and 'two back' accumulators"""
        if n == 0:
            return 1
        if n == 1:
            return 1
        fib_counter: int = 2
        fib_one_back: int = 1
        fib_two_back: int = 1
        fib_current: int = 0

        while fib_counter <= n:
            fib_current = fib_one_back + fib_two_back
            fib_two_back = fib_one_back
            fib_one_back = fib_current
            fib_counter += 1

        return fib_current



# find the sum of even Fibonacci numbers less than or equal to 4,000,000
fibonacci = Fibonacci()
benchmark = bench_timer.Benchmark()
fib_sum = 0
halt = False
index = 0

benchmark.start()
while not halt:
    fib_out = fibonacci.fib(index)
    if fib_out > 4000000:
        halt = True
        break
    if fib_out % 2 == 0:
        fib_sum += fib_out
        print(f'{index}: {fib_out}')
    index += 1

print(f'sum of even Fibonacci numbers <= 4M: {fib_sum}')
benchmark.end()

print(f'try: {math.log(23, 10)}')

# test_n = 43365644
test_n = 200
print([(test_n//(10**i)) % 10 for i in range(math.ceil(math.log(test_n, 10))-1, -1, -1)])

print(f'\nrecursive method (n = {test_n}):')
benchmark.start()
result_1 = fibonacci.fib(test_n)
benchmark.end()
print(f'method 1 result: {result_1}\n')

print(f'cumulative method: (n = {test_n})')
benchmark.start()
result_2 = fibonacci.fib_in_constant_space(test_n)
benchmark.end()
print(f'method 1 result: {result_2}\n')
