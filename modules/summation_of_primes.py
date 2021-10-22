# Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import primes
import bench_timer

p = primes.Primes()
bt = bench_timer.Benchmark()

primes_range: int = 2000000

# sum of primes below 10 (mehtod 1)
# print('\nmethod 1...')
# primes_sum: int = 0
# bt.start()
# for i in range (1,primes_range):
#     if p.is_prime(i):
#         primes_sum += i
# bt.end()
# print(f'primes_sum below {primes_range}: {primes_sum}')

# sum of primes below primes_range (method 2)
print('\nmethod 2...')
primes_sum: int = 0
bt.start()
primes_in_range = p.prime_numbers(primes_range - 1)
for prime_number in primes_in_range:
    primes_sum += prime_number
bt.end()
print(f'primes_sum below {primes_range}: {primes_sum}')

