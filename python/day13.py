from math import prod

def parse(lines):
    start = int(lines[0])
    buses = [int(x) if x.isnumeric() else None for x in lines[1].split(',')]
    return start, buses

def day13a(start, buses):
    first = min((b for b in buses if b), key=lambda b: b - (start % b))
    wait = first - (start % first)
    return first * wait

# from https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html (under "For Several Equations")
# plus going down a rabbit hole of solving linear congruences and diophantane equations
#       https://www.dave4math.com/mathematics/chinese-remainder-theorem/
#       https://www.dave4math.com/mathematics/linear-congruences/
#       https://www.dave4math.com/mathematics/diophantine-equations/
# plus learning that `A ≡ B (mod C)` really means `A mod C = B mod C`
#       https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/congruence-modulo
# plus learning that calculating b' from that first link is called the modular multiplicative inverse
# plus learning that python 3.8+ now has pow() that can do modular exponentiation
#       https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

def crt(L):
    N = prod(n for (_, n) in L)
    return sum(a * (N//n) * pow(N//n, -1, n) for (a, n) in L), N

def day13b(buses):
    x, N = crt([(a, n) for (a, n) in enumerate(buses) if n is not None])
    return N - (x % N)

def test_13_ex1(): assert day13a(*parse(ex1)) == 295

# examples from https://www.dave4math.com/mathematics/chinese-remainder-theorem/
def test_13_crt1(): assert crt([(2, 3), (5, 4), (-3, 7)]) == (53, 84)
def test_13_crt2(): assert crt([(3, 5), (2, 6), (4, 7)]) == (1208, 210)
def test_13_crt3(): assert crt([(2, 3), (3, 5), (2, 7)]) == (233, 105)
def test_13_crt4(): assert crt([(1, 2), (2, 3), (3, 5), (4, 7)]) == (1103, 210)

def test_13_ex2a(): assert day13b(parse(ex1)[1]) == 1068781
def test_13_ex2b(): assert day13b([17, None, 13, 19]) == 3417
def test_13_ex2c(): assert day13b([67, 7, 59, 61]) == 754018
def test_13_ex2d(): assert day13b([67, None, 7, 59, 61]) == 779210
def test_13_ex2e(): assert day13b([67, 7, None, 59, 61]) == 1261476
def test_13_ex2f(): assert day13b([1789, 37, 47, 1889]) == 1202161486

def test_13a(day13_lines): assert day13a(*parse(day13_lines)) == 2045
def test_13b(day13_lines): assert day13b( parse(day13_lines)[1]) == 402251700208309

ex1 = ['939', '7,13,x,x,59,x,31,19']
