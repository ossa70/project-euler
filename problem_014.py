# Longest Collatz Sequence

n = 1000000

cache = {1: 1}

def collatz_length(n):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        length = 1 + collatz_length(n // 2)
    else:
        length = 1 + collatz_length(3 * n + 1)
    cache[n] = length
    return length

best = 0
number = None

for i in range(1, n):
    length = collatz_length(i)
    if length > best:
        best = length
        number = i

print(best, number)