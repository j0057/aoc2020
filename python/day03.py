import math

def parse(lines):
    return {x + y * 1j
            for (y, line) in enumerate(lines)
            for (x, char) in enumerate(line)
            if char == '#'}, len(lines[0]), len(lines)

def traverse_map(trees, w, h, pos, vec):
    count = 0
    while pos.imag < h:
        count += pos in trees
        pos += vec
        if pos.real >= w:
            pos = complex(pos.real % w, pos.imag)
    return count

def day03a(lines): return traverse_map(*parse(lines), 0+0j, 3+1j)

def day03b(lines): return math.prod(traverse_map(*parse(lines), 0+0j, v)
                                    for v in [1+1j, 3+1j, 5+1j, 7+1j, 1+2j])

ex=['..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#']

def test_03_parse1(): assert 2+0j in parse(ex)[0]
def test_03_parse2(): assert parse(ex)[1] == 11
def test_03_parse3(): assert parse(ex)[2] == 11

def test_03_ex1(): assert day03a(ex) == 7
def test_03_ex2(): assert day03b(ex) == 336

def test_03a(day03_lines): assert day03a(day03_lines) == 171
def test_03b(day03_lines): assert day03b(day03_lines) == 1206576000
