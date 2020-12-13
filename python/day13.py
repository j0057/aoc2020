from itertools import count

def parse(lines):
    start = int(lines[0])
    buses = [int(x) if x.isnumeric() else None for x in lines[1].split(',')]
    return start, buses

def day13a(start, buses):
    first = min((b for b in buses if b), key=lambda b: b - (start % b))
    wait = first - (start % first)
    return first * wait

def day13b(buses):
    return next(t for t in count(start=0, step=buses[0])
                if all(b - (t % b) == i
                       for (i, b) in enumerate(buses)
                       if i and b))

def test_13_ex1(): assert day13a(*parse(ex1)) == 295

def test_13_ex2a(): assert day13b(parse(ex1)[1]) == 1068781
def test_13_ex2b(): assert day13b([17, None, 13, 19]) == 3417
def test_13_ex2c(): assert day13b([67, 7, 59, 61]) == 754018
def test_13_ex2d(): assert day13b([67, None, 7, 59, 61]) == 779210
def test_13_ex2e(): assert day13b([67, 7, None, 59, 61]) == 1261476
def test_13_ex2f(): assert day13b([1789, 37, 47, 1889]) == 1202161486

def test_13a(day13_lines): assert day13a(*parse(day13_lines)) == 2045
def _est_13b(day13_lines): assert day13b( parse(day13_lines)[1]) == None

ex1 = ['939', '7,13,x,x,59,x,31,19']
