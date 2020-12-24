from collections import Counter

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

def day24a(paths):
    counts = Counter(sum(path) for path in paths)
    return sum(count % 2 == 1 for count in counts.values())

def test_24_ex1(): assert day24a(parse(ex1)) == 10
def test_24_ex2(): assert day24a(parse(ex1)) == 10

def test_24a(day24_lines): assert day24a(parse(day24_lines)) == 391

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
