# Project Euler Solutions

My solutions to [Project Euler](https://projecteuler.net/) problems, written in Python.

This repo is part of my practice rebuilding Python fluency, ahead of applying it to
production/maintenance scheduling optimization (MILP, Gurobi/OR-Tools/Pyomo).

## Progress

| Problem | Title | Solution | Key concepts applied |
|---------|---------------------------------|----------------------------------------|-----------------------|
| 0 (practice, not official) | Sum of odd squares | [problem_000.py](problem_000.py) | Generator expressions vs. list comprehensions |
| 1 | Multiples of 3 or 5 | [problem_001.py](problem_001.py) | Generator expressions; filtering with modulo |
| 2 | Even Fibonacci numbers | [problem_002.py](problem_002.py) | Sequence generation; avoiding redundant/duplicate terms |
| 3 | Largest prime factor | [problem_003.py](problem_003.py) | Trial division bounded by √n; recovering the final leftover factor |
| 4 | Largest palindrome product | [problem_004.py](problem_004.py) | Symmetry to halve brute force; early-exit bounds on nested loops |
| 5 | Smallest multiple | [problem_005.py](problem_005.py) | GCD/LCM via the Euclidean algorithm; hand-rolling vs. `math.gcd`/`math.lcm` |
| 6 | Sum square difference | [problem_006.py](problem_006.py) | Generator expressions |
| 7 | 10001st prime | [problem_007.py](problem_007.py) | √n primality bound; Big-O growth; hidden cost of list slicing |
| 8 | Largest product in a series | [problem_008.py](problem_008.py) | `math.prod`; avoiding magic numbers |
| 9 | Special Pythagorean triplet | [problem_009.py](problem_009.py) | Deriving values from constraints instead of looping; valid vs. "cheating" bounds; Big-O analysis |
| 10 | Summation of primes | [problem_010.py](problem_010.py) | Sieve of Eratosthenes vs. trial division; `bytearray` for memory efficiency |
| 11 | Largest product in a grid | [problem_011.py](problem_011.py) | Correctly scoping conditionals; DRY refactor to prevent recurring bugs; parametrizing magic numbers |
| 12 | Highly divisible triangular number | [problem_012.py](problem_012.py) | Infinite generators (`itertools.count`/`accumulate`); divisor-pair counting; perfect-square edge cases |
| 13 | Large sum | [problem_013.py](problem_013.py) | Avoiding shadowing Python built-ins |
| 14 | Longest Collatz sequence | [problem_014.py](problem_014.py) | Recursion with memoization; dict vs. list for lookups; Python's recursion limit |
| 15 | Lattice paths | [problem_015.py](problem_015.py) | Dynamic programming (build from a known base case); recognizing when brute force is infeasible; `functools.lru_cache` |
| 16 | Power digit sum | [problem_016.py](problem_016.py) | Python's native big-integer support; digit-summing via string conversion |
| 17 | Number letter counts | [problem_017.py](problem_017.py) | Modular string-building with reusable lookups; DRY refactor by generalizing a helper's scope |
| 18 | Maximum path sum I | [problem_018.py](problem_018.py) | Bottom-up dynamic programming on a triangle; shallow vs. deep copies |

## Running a solution

```bash
uv venv
source .venv/bin/activate
python problem_001.py