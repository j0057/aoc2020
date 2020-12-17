from functools import reduce
from itertools import islice, product

extremes = lambda seq, dim: (min(p[dim] for p in seq), max(p[dim] for p in seq))
itercoord = lambda seq, dim: (lambda lo, hi: range(lo-1, hi+2))(*extremes(seq, dim))
nth = lambda seq, n: next(islice(seq, n, None), None)

def parse(lines, D):
    return {(x, y) + tuple(0 for _ in range(D-2))
            for (y, line) in enumerate(lines)
            for (x, char) in enumerate(line) if char == '#'}

def evolve(state, D):
    offset = [o for o in product([-1, 0, +1], repeat=D) if any(o)]
    counts = lambda state: ((p, sum(tuple(a+b for (a,b) in zip(p, q)) in state for q in offset))
                            for p in product(*[itercoord(state, d) for d in range(D)]))
    while state:
        yield state
        state = {p for (p, c) in counts(state)
                 if (c in {2, 3} if p in state else c == 3)}

def day17(state, D, n=6): return nth((len(state) for state in evolve(state, D)), n)

ex1 = '.#.|..#|###'.split('|')

def test_17_ex1a(): assert day17(parse(ex1, 3), 3, n=0) == 5
def test_17_ex1b(): assert day17(parse(ex1, 3), 3, n=1) == 11
def test_17_ex1c(): assert day17(parse(ex1, 3), 3, n=2) == 21
def test_17_ex1d(): assert day17(parse(ex1, 3), 3, n=3) == 38
def test_17_ex1e(): assert day17(parse(ex1, 3), 3, n=6) == 112

def test_17_ex2a(): assert day17(parse(ex1, 4), 4, n=0) == 5
def test_17_ex2b(): assert day17(parse(ex1, 4), 4, n=1) == 29

def test_17a(day17_lines): assert day17(parse(day17_lines, 3), 3) == 319
def test_17b(day17_lines): assert day17(parse(day17_lines, 4), 4) == 2324
