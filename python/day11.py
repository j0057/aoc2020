def parse(lines):
    return {(y, x): state for (y, line) in enumerate(lines)
                          for (x, state) in enumerate(line)
                          if state == 'L'}

def iterate(state):
    while True:
        state = {(y, x): '#' if all(state.get((y+dy, x+dx), '.') in {'L', '.'} for dy in [-1, 0, +1] for dx in [-1, 0, +1] if dy or dx)      else
                         'L' if sum(state.get((y+dy, x+dx), '.') == '#'        for dy in [-1, 0, +1] for dx in [-1, 0, +1] if dy or dx) >= 4 else state[y, x]
                 for (y, x) in state}
        yield state

def day11a(state):
    for state_ in iterate(state):
        if state == state_:
            return sum(v == '#' for v in state_.values())
        state = state_

ex1 = 'L.LL.LL.LL|LLLLLLL.LL|L.L.L..L..|LLLL.LL.LL|L.LL.LL.LL|L.LLLLL.LL|..L.L.....|LLLLLLLLLL|L.LLLLLL.L|L.LLLLL.LL'.split('|')

def test_11_parse1(): assert parse(ex1).get((0, 0), '.') == 'L'
def test_11_parse2(): assert parse(ex1).get((0, 1), '.') == '.'

def test_11_ex1(): assert day11a(parse(ex1)) == 37

def test_11a(day11_lines): assert day11a(parse(day11_lines)) == 2126
