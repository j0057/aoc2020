def day10a(J):
    J = [0] + sorted(J) + [max(J)+3]
    return sum(b-a == 1 for (a,b) in zip(J, J[1:])) \
         * sum(b-a == 3 for (a,b) in zip(J, J[1:]))


ex1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
ex2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

def test_10_ex2(): assert day10a(ex2) == 220

def test_10a(day10_numbers): assert day10a(day10_numbers) == 2475
