def parse(lines):
    start = int(lines[0])
    buses = [int(x) if x.isnumeric() else None for x in lines[1].split(',')]
    return start, buses

def day13a(start, buses):
    first = min((b for b in buses if b), key=lambda b: b - (start % b))
    wait = first - (start % first)
    return first * wait

def test_13_ex1(): assert day13a(*parse(ex1)) == 295

def test_13a(day13_lines): assert day13a(*parse(day13_lines)) == 2045

ex1 = ['939', '7,13,x,x,59,x,31,19']
