# Special Pythagorean Triplet

sum_goal = 1000

finished = False

for c in range (335, 999):
    if finished:
        break
    for b in range(2, c):
        a = sum_goal - b - c
        if a > b or a < 1:
             continue
        if a**2 + b**2 == c**2:
                print(a, b, c, a*b*c)
                finished = True
                break
