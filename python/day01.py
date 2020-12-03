from itertools import combinations
from math import prod

def report_repair(expenses, *, n=2):
    for entries in combinations(expenses, n):
        if sum(entries)== 2020:
            return prod(entries)

def day01a(expenses): return report_repair(expenses)
def day01b(expenses): return report_repair(expenses, n=3)

def test_01_ex1(): assert day01a([1721, 979, 366, 299, 675, 1456]) == 514579
def test_01_ex2(): assert day01b([1721, 979, 366, 299, 675, 1456]) == 241861950

def test_01a(day01_numbers): assert day01a(day01_numbers) == 538464
def test_01b(day01_numbers): assert day01b(day01_numbers) == 278783190
