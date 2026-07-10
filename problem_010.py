# Summation of Primes

import math

stop = 2_000_000

# My original approach: trial division against known primes (works, but slower)
# prime_numbers = [2]
#
# i = 3
#
# while i < stop:
#     prime = True
#     isq = math.isqrt(i)
#     for j in prime_numbers:
#         if j > isq:
#             break
#         if i % j == 0:
#             prime = False
#             break
#     if prime:
#         prime_numbers.append(i)
#     i += 2
#
# print(sum(prime_numbers))

# Sieve of Eratosthenes (technique shown to me by Claude) -- much faster for large ranges
sieve = bytearray([1]) * stop
sieve[0] = sieve[1] = 0
for i in range(2, math.isqrt(stop)+1):
    if sieve[i]:
        for multiple in range(i*i, stop, i):
            sieve[multiple] = 0
total = sum(i for i, is_p in enumerate(sieve) if is_p)
print(total)
