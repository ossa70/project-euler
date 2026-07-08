# What is the 10001st prime number?
import math

n = 10001

prime_numbers = [2]

i = 3
while len(prime_numbers) < n:
    prime = True
    isq = math.isqrt(i)
    for j in prime_numbers:
        if j > isq:
            break
        if i % j == 0:
            prime = False
            break
    if prime:
        prime_numbers.append(i)
    i += 2
        
print(prime_numbers[-1])