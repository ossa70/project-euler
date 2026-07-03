# Sum of even Fibonacci number that don't exceed 4 million
def fib(x):
    """Returns the fibonacci sequence up to x"""
    a, b = 1, 2
    fibo = []
    while a <= x:
        fibo.append(a)
        a, b = b, a+b

    return fibo

fibo = fib(4_000_000)
sum_even_fibo = sum((x for x in fibo if x % 2 == 0))
print(sum_even_fibo)