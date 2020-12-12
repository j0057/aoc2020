from collections import deque

manhattan = lambda n: abs(n.real) + abs(n.imag)
last = lambda L: deque(L, maxlen=1).pop()

def navigate(L, p=0+0j, v=1+0j, m=1):
    for cmd, n in [(x[0], int(x[1:])) for x in L]:
        if   m==1 and cmd == 'N': p += n * (+0-1j)
        elif m==1 and cmd == 'E': p += n * (+1+0j)
        elif m==1 and cmd == 'S': p += n * (+0+1j)
        elif m==1 and cmd == 'W': p += n * (-1+0j)
        elif m==2 and cmd == 'N': v += n * (+0-1j)
        elif m==2 and cmd == 'E': v += n * (+1+0j)
        elif m==2 and cmd == 'S': v += n * (+0+1j)
        elif m==2 and cmd == 'W': v += n * (-1+0j)
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
def day12b(lines): return manhattan(last(navigate(lines, v=10-1j, m=2))[0])

def test_12_ex1a(): assert [*navigate(ex1)] == [(10+0j, 1+0j), (10-3j, 1+0j), (17-3j, 1+0j), (17-3j, 0+1j), (17+8j, 0+1j)]
def test_12_ex1b(): assert day12a(ex1) == 25

def test_12_ex2a(): assert [*navigate(ex1, v=10-1j, m=2)] == [(100-10j, 10-1j), (100-10j, 10-4j), (170-38j, 10-4j), (170-38j, 4+10j), (214+72j, 4+10j)]
def test_12_ex2b(): assert day12b(ex1) == 286

def test_12a(day12_lines): assert day12a(day12_lines) == 938
def test_12b(day12_lines): assert day12b(day12_lines) == 54404

ex1 = 'F10|N3|F7|R90|F11'.split('|')
