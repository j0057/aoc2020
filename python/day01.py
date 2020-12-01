from itertools import combinations
from functools import reduce

def report_repair(expenses, *, n=2):
    for entries in combinations(expenses, n):
        if sum(entries)== 2020:
            return reduce(lambda a, b: a * b, entries, 1)

def test_01_ex1():
    assert report_repair([1721, 979, 366, 299, 675, 1456]) == 514579

def test_01a(day01_numbers):
    assert report_repair(day01_numbers) == 538464
