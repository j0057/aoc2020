from itertools import islice, count
from collections import defaultdict, deque

nth = lambda seq, i: next(islice(seq, i, None), None)

def parse(text):
    return [int(x) for x in text.split(',')]

def memory_game(initial):
    ages = defaultdict(lambda: deque(maxlen=2))
    for t, n in enumerate(initial):
        yield n
        ages[n].appendleft(t+1)
    for turn in count(len(initial)+1):
        n = ages[n][0] - ages[n][-1] if len(ages[n]) == 2 else 0
        ages[n].appendleft(turn)
        yield n

def day15a(initial): return nth(memory_game(initial), 2020-1)
def day15b(initial): return nth(memory_game(initial), 30000000-1)

def test_15_ex0(): assert [*islice(memory_game([0, 3, 6]), 0, 10)] == [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]

def test_15_ex1(): assert day15a([1, 3, 2]) == 1
def test_15_ex2(): assert day15a([2, 1, 3]) == 10
def test_15_ex3(): assert day15a([1, 2, 3]) == 27
def test_15_ex4(): assert day15a([2, 3, 1]) == 78
def test_15_ex5(): assert day15a([3, 2, 1]) == 438
def test_15_ex6(): assert day15a([3, 1, 2]) == 1836

def test_15a(day15_text): assert day15a(parse(day15_text)) == 1294
def test_15b(day15_text): assert day15b(parse(day15_text)) == 573522
