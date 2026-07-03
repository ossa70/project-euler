# This was actually problem 0, just to register
# Sum of the first 254000 square odd numbers
n = 254000
squares = [x**2 for x in range(1, n+1) if x**2 % 2 != 0]
sum_squares = sum(squares)
print(sum_squares)

# Problem 1
#sum of all the multiples of 3 or 5 below 1000
n = 1000
multiples = [x for x in range(1, n) if x % 3 == 0 or x % 5 == 0]
sum_multiples = sum(multiples)
print(multiples)
print(sum_multiples)