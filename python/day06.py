from functools import reduce
from itertools import chain

def day06a(text): return sum(len({*chain(*group.split())}) for group in text.split('\n\n'))
def day06b(text): return sum(len(reduce(lambda a, b: a & b, [{*g} for g in group.split()]))
                             for group in text.split('\n\n'))

ex = 'abc||a|b|c||ab|ac||a|a|a|a||b|'.replace('|', '\n')

def test_06_ex1(): assert day06a(ex) == 11
def test_06_ex2(): assert day06b(ex) == 6

def test_06a(day06_text): assert day06a(day06_text) == 6506
def test_06b(day06_text): assert day06b(day06_text) == 3243
