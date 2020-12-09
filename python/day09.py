from itertools import combinations

def find_non_sum(L, p=25, r=2):
    return next(n for (i, n) in enumerate(L)
                if i >= p and not any(n == sum(c) for c in combinations(L[i-p:i], r)))

ex1 = [*range(1, 26), 26, 49, 100, 50]
ex2 = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

def test_09_ex1(): assert find_non_sum(ex1, 25) == 100
def test_09_ex2(): assert find_non_sum(ex2, 5) == 127

def test_09a(day09_numbers): assert find_non_sum(day09_numbers, 25, 2) == 1721308972
