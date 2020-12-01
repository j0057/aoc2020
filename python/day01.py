from itertools import combinations
from functools import reduce
import operator

def report_repair(expenses, *, n=2):
    for entries in combinations(expenses, n):
        if sum(entries)== 2020:
            return reduce(operator.mul, entries, 1)

def test_01_ex1():
    assert report_repair([1721, 979, 366, 299, 675, 1456]) == 514579

def test_01_ex2():
    assert report_repair([1721, 979, 366, 299, 675, 1456], n=3) == 241861950

def test_01a(day01_numbers):
    assert report_repair(day01_numbers) == 538464

def test_01b(day01_numbers):
    assert report_repair(day01_numbers, n=3) == 278783190
