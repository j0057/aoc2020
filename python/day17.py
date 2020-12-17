from functools import reduce
from itertools import islice
from more_itertools import iterate

extremes = lambda seq, dim: (min(p[dim] for p in seq), max(p[dim] for p in seq))
itercoord = lambda seq, dim: (lambda lo, hi: range(lo-1, hi+2))(*extremes(seq, dim))
nth = lambda seq, n: next(islice(seq, n, None), None)

def parse(lines):
    return {(x, y, 0) for (y, line) in enumerate(lines)
                      for (x, char) in enumerate(line) if char == '#'}

def evolve(state):
    counts = lambda state: ((x, y, z, sum((x+dx, y+dy, z+dz) in state
                                          for dx in [-1, 0, +1]
                                          for dy in [-1, 0, +1]
                                          for dz in [-1, 0, +1] if dx or dy or dz))
                            for x in itercoord(state, 0)
                            for y in itercoord(state, 1)
                            for z in itercoord(state, 2))
    return iterate(lambda state: {(x, y, z)
                                  for (x, y, z, c) in counts(state)
                                  if (c in {2, 3} if (x, y, z) in state else c == 3)}, state)

def day17a(state, n=6): return nth((len(state) for state in evolve(state)), n)

ex1 = '.#.|..#|###'.split('|')

def test_17_ex1a(): assert day17a(parse(ex1), n=0) == 5
def test_17_ex1b(): assert day17a(parse(ex1), n=1) == 11
def test_17_ex1c(): assert day17a(parse(ex1), n=2) == 21
def test_17_ex1d(): assert day17a(parse(ex1), n=3) == 38
def test_17_ex1e(): assert day17a(parse(ex1), n=6) == 112

def test_17a(day17_lines): assert day17a(parse(day17_lines)) == 319
