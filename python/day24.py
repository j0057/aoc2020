from collections import Counter
from functools import reduce
from itertools import islice
from math import inf

nth = lambda seq, n: next(islice(seq, n, None), None)

def parse(lines):
    def steps(s):
        while s:
            r, s = (+0-1j, s[2:]) if s[:2] == 'nw' else \
                   (+1-1j, s[2:]) if s[:2] == 'ne' else \
                   (-1+1j, s[2:]) if s[:2] == 'sw' else \
                   (+0+1j, s[2:]) if s[:2] == 'se' else \
                   (-1+0j, s[1:]) if s[:1] == 'w'  else \
                   (+1+0j, s[1:]) if s[:1] == 'e'  else 1/0
            yield r
    return [[*steps(line)] for line in lines]

def iter_grid(tiles):
    bbox = lambda seq: reduce(lambda a, b: (min(a[0], b.imag), max(a[1], b.imag), min(a[2], b.real), max(a[3], b.real)), seq, (+inf, -inf, +inf, -inf))
    T, B, L, R = bbox(tiles)
    return (c + r * 1j for r in range(int(T)-1, int(B)+2) for c in range(int(L)-1, int(R)+2))

def day24a(paths):
    counts = Counter(sum(path) for path in paths)
    return sum(count % 2 == 1 for count in counts.values())

def day24b(paths):
    counts = Counter(sum(path) for path in paths)
    tiles = {p for (p, c) in counts.items() if c % 2 == 1}
    while True:
        tiles = {n for (n, c) in ((n, sum((n+m) in tiles for m in [-1j, +1-1j, -1+1j, 1j, -1, 1]))
                                  for n in iter_grid(tiles))
                   if (c in {1, 2} if n in tiles else c == 2)}
        yield tiles

def test_24_ex1(): assert day24a(parse(ex1)) == 10
def test_24_ex2(): assert day24a(parse(ex1)) == 10

def test_24_ex3(): assert [*islice((len(g) for g in day24b(parse(ex1))),  1-1,  10,  1)] == [15, 12, 25, 14, 23, 28, 41, 37, 49, 37]
def test_24_ex4(): assert [*islice((len(g) for g in day24b(parse(ex1))), 20-1, 100, 10)] == [132, 259, 406, 566, 788, 1106, 1373, 1844, 2208]

def test_24a(day24_lines): assert day24a(parse(day24_lines)) == 391

def test_24b(day24_lines): assert len(nth(day24b(parse(day24_lines)), 100-1)) == 3876

ex1 = ['sesenwnenenewseeswwswswwnenewsewsw',
       'neeenesenwnwwswnenewnwwsewnenwseswesw',
       'seswneswswsenwwnwse',
       'nwnwneseeswswnenewneswwnewseswneseene',
       'swweswneswnenwsewnwneneseenw',
       'eesenwseswswnenwswnwnwsewwnwsene',
       'sewnenenenesenwsewnenwwwse',
       'wenwwweseeeweswwwnwwe',
       'wsweesenenewnwwnwsenewsenwwsesesenwne',
       'neeswseenwwswnwswswnw',
       'nenwswwsewswnenenewsenwsenwnesesenew',
       'enewnwewneswsewnwswenweswnenwsenwsw',
       'sweneswneswneneenwnewenewwneswswnese',
       'swwesenesewenwneswnwwneseswwne',
       'enesenwswwswneneswsenwnewswseenwsese',
       'wnwnesenesenenwwnenwsewesewsesesew',
       'nenewswnwewswnenesenwnesewesw',
       'eneswnwswnwsenenwnwnwwseeswneewsenese',
       'neswnwewnwnwseenwseesewsenwsweewe',
       'wseweeenwnesenwwwswnew']
