# Lattice Paths

size = 20

grid = []

for i in range(size + 1):
    grid.append([])
    for j in range(size + 1):
        if i == 0 or j == 0:
            grid[i].append(1)
        else:
            grid[i].append(grid[i][j-1] + grid[i-1][j])

print(grid[-1][-1])

# Same recurrence, implemented recursively with memoization (for comparison)
from functools import lru_cache

@lru_cache(maxsize=None)
def paths(i, j):
    if i == 0 or j == 0:
        return 1
    return paths(i-1, j) + paths(i, j-1)

print(paths(size, size))