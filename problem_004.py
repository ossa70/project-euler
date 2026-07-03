# Find the largest palindrome made from the product of two 3-digit numbers.
best = 0
for i in range(999, 99, -1):
    if 999 * i < best:
        break
    for j in range(999, i-1, -1):
        number = i * j
        if number < best:
            break
        number_str = str(number)
        reversed_n = number_str[::-1]
        if number_str == reversed_n and number > best:
            best = number
print(best)