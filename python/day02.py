import re

def parse(passwords):
    return (re.match(r'^(\d+)-(\d+) (\w): (\w+)$', line).groups() for line in passwords)

def day02a(passwords):
    return sum(int(lo) <= pwd.count(ltr) <= int(hi) for (lo, hi, ltr, pwd) in parse(passwords))

def test_02_ex1(): assert day02a(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']) == 2

def test_02a(day02_lines): assert day02a(day02_lines) == 378
