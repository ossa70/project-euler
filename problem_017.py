# Number Letter Counts

end = 1000

words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}

counter = 0

def two_digit_length(x):
    if x == 0:
        return 0
    if x in words:
        return len(words[x])
    return len(words[(x//10)*10]) + len(words[x%10])

for n in range(1, end + 1):
    if n < 100:
        counter += two_digit_length(n)
    elif n < 1000:
        counter += len(words[n//100]) + len(words[100])
        remainder = n % 100
        if remainder != 0:
            counter += len("and") + two_digit_length(remainder)
    else:
        counter += len(words[n//1000]) + len(words[1000])

print(counter)