from collections import deque

manhattan = lambda n: abs(n.real) + abs(n.imag)
last = lambda L: deque(L, maxlen=1).pop()

def navigate(L, p=0+0j, v=1+0j):
    for cmd, n in [(x[0], int(x[1:])) for x in L]:
        if   cmd == 'N': p += n * (+0-1j)
        elif cmd == 'E': p += n * (+1+0j)
        elif cmd == 'S': p += n * (+0+1j)
        elif cmd == 'W': p += n * (-1+0j)
        elif cmd == 'F': p += n * v
        elif cmd == 'R':
            for _ in range(n//90):
                v *= +1j
        elif cmd == 'L':
            for _ in range(n//90):
                v *= -1j
        else: raise Exception(f"WTF? {cmd}{n}")
        yield p, v

def day12a(lines): return manhattan(last(navigate(lines))[0])

def test_12_ex1a(): assert [*navigate(ex1)] == [(10+0j, 1+0j), (10-3j, 1+0j), (17-3j, 1+0j), (17-3j, 0+1j), (17+8j, 0+1j)]
def test_12_ex1b(): assert day12a(ex1) == 25

def test_12a(day12_lines): assert day12a(day12_lines) == 938

ex1 = 'F10|N3|F7|R90|F11'.split('|')
