from itertools import chain

def day06a(text): return sum(len({*chain(*group.split())}) for group in text.split('\n\n'))

ex = 'abc||a|b|c||ab|ac||a|a|a|a||b|'.replace('|', '\n')

def test_06_ex1(): assert day06a(ex) == 11

def test_06a(day06_text): assert day06a(day06_text) == 6506
