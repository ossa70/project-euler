# Problem 1
#sum of all the multiples of 3 or 5 below 1000
n = 1000
multiples = (x for x in range(1, n) if x % 3 == 0 or x % 5 == 0)
sum_multiples = sum(multiples)
print(sum_multiples)