from itertools import combinations, count

def find_non_sum(L, p=25, r=2):
    return next(n for (i, n) in enumerate(L)
                if i >= p and not any(n == sum(c) for c in combinations(L[i-p:i], r)))

def find_weak_range(L, x):
    return next(min(L[i:i+c]) + max(L[i:i+c])
                for c in count(2)
                for i in range(len(L)-c)
                if sum(L[i:i+c]) == x)

ex1 = [*range(1, 26), 26, 49, 100, 50]
ex2 = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

def test_09_ex1(): assert find_non_sum(ex1, 25) == 100
def test_09_ex2(): assert find_non_sum(ex2, 5) == 127

def test_09_ex3(): assert find_weak_range(ex2, find_non_sum(ex2, 5)) == 62

def test_09a(day09_numbers): assert find_non_sum(day09_numbers, 25, 2) == 1721308972
def test_09b(day09_numbers): assert find_weak_range(day09_numbers, find_non_sum(day09_numbers)) == 209694133
