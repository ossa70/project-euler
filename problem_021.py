# Amicable Numbers
import math

max_number = 10000

def d_n(n):

    div_sum = 1

    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            div_sum += i
            if i != n//i:
                div_sum += n//i

    return div_sum

data = {}

for i in range(2, max_number + 1):
    data[i] = d_n(i)

def sum_proper_divisors(x):
    return data[x] if x <= max_number else d_n(x)

amicable_num = set()

for i, d_i in data.items():
    if i in amicable_num or d_i == 1:
        continue
    if sum_proper_divisors(d_i) == i and i != d_i:
        amicable_num.add(i)
        if d_i <= max_number:
            amicable_num.add(d_i)


print(sum(amicable_num))