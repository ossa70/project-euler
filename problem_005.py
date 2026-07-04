# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

n = 20

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b // gcd(a, b))

current_lcm = 1
for i in range(1, n+1):
    current_lcm = lcm(current_lcm, i)

print(current_lcm)