def seat_id(spec):
    n = spec.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
    r = int(n[:7], 2)
    c = int(n[7:], 2)
    return r, c, r*8 + c

def day05a(specs): return max(seat_id(s)[2] for s in specs)

def test_05_ex1(): assert seat_id('BFFFBBFRRR') == (70, 7, 567)
def test_05_ex2(): assert seat_id('FFFBBBFRRR') == (14, 7, 119)
def test_05_ex3(): assert seat_id('BBFFBBFRLL') == (102, 4, 820)

def test_05a(day05_lines): assert day05a(day05_lines) == 919
