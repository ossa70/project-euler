# This was actually problem 0, just to register
# Sum of the first 254000 odd square numbers
n = 254000
squares = (x**2 for x in range(1, n+1, 2))
sum_odd_squares = sum(squares)
print(sum_odd_squares)
