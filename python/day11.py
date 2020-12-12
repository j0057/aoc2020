from collections import defaultdict

def parse(lines):
    return {(y, x): state for (y, line) in enumerate(lines)
                          for (x, state) in enumerate(line)
                          if state == 'L'}

def iterate(state, max_r, t):
    N = defaultdict(lambda: [])
    for (y, x) in state:
        for dy in [-1, 0, +1]:
            for dx in [-1, 0, +1]:
                if not dy and not dx:
                    continue
                for r in range(1, max_r+1):
                    ny, nx = y+dy*r, x+dx*r
                    if state.get((ny, nx), '.') == 'L':
                        N[y, x].append((ny, nx))
                        break
    while True:
        state = {(y, x): '#' if c == 0 else
                         'L' if c >= t else state[y, x]
                 for (y, x, c) in ((y, x, [state[n] for n in N[y, x]].count('#')) for (y, x) in state)}
        yield state

def day11a(state, max_r=1, tolerance=4):
    for state_ in iterate(state, max_r, tolerance):
        if state == state_:
            return sum(v == '#' for v in state_.values())
        state = state_

ex1 = 'L.LL.LL.LL|LLLLLLL.LL|L.L.L..L..|LLLL.LL.LL|L.LL.LL.LL|L.LLLLL.LL|..L.L.....|LLLLLLLLLL|L.LLLLLL.L|L.LLLLL.LL'.split('|')

def test_11_parse1(): assert parse(ex1).get((0, 0), '.') == 'L'
def test_11_parse2(): assert parse(ex1).get((0, 1), '.') == '.'

def test_11_ex1(): assert day11a(parse(ex1)) == 37
def test_11_ex2(): assert day11a(parse(ex1), max_r=10, tolerance=5) == 26

def test_11a(day11_lines): assert day11a(parse(day11_lines)) == 2126
def test_11b(day11_lines): assert day11a(parse(day11_lines), max_r=90, tolerance=5) == 1914
