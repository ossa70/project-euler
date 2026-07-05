# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = 100

sum_squares = sum(i**2 for i in range(1, n+1))
square_sum = sum(i for i in range(1, n+1))**2
dif = square_sum - sum_squares
print(dif)