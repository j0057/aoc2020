def seat_id(spec):
    return int(spec.translate(str.maketrans('FBRL', '0110')), 2)

def day05a(specs): return max(seat_id(s) for s in specs)
def day05b(specs):
    seats = {seat_id(s) for s in specs}
    return next(s for s in range(max(seats)+1)
                if s not in seats and s+1 in seats and s-1 in seats)

def test_05_ex1(): assert seat_id('BFFFBBFRRR') == 567
def test_05_ex2(): assert seat_id('FFFBBBFRRR') == 119
def test_05_ex3(): assert seat_id('BBFFBBFRLL') == 820

def test_05a(day05_lines): assert day05a(day05_lines) == 919
def test_05b(day05_lines): assert day05b(day05_lines) == 642
