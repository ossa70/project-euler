# Largest prime factor of 600851475143
n = 600851475143
d = 2
factors = []
while d * d < n:
    while n % d == 0:
        n = int(n / d)
        factors.append(d)
    d+=1
factors = set(factors)
if len(factors) == 0:
    print(n)
elif n > max(factors):
    print(n)
else:
    print(max(factors))