from itertools import combinations

def report_repair(expenses):
    for (a, b) in combinations(expenses, 2):
        if a + b == 2020:
            return a * b

def test_01_ex1():
    assert report_repair([1721, 979, 366, 299, 675, 1456]) == 514579

def test_01a(day01_numbers):
    assert report_repair(day01_numbers) == 538464
