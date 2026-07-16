# Highly Divisible Triangular Number

from itertools import count, accumulate
import math

req_divisors = 500

tri_num = accumulate(count(1))

for t in tri_num:

    divisors = 2

    for i in range(2, math.isqrt(t)+1):
        if t % i == 0:
            divisors += 1
            if i != t//i:
                divisors += 1

    if divisors > req_divisors:
        result = t
        break

print(result)