from itertools import takewhile
from more_itertools import iterate
import math

def traverse_map(trees, y, x, dy, dx):
    path = iterate(lambda p: (p[0] + dy, (p[1] + dx) % len(trees[0])), start=(0, 0))
    return sum(trees[y][x] == '#' for (y, x) in takewhile(lambda p: p[0] < len(trees), path))

def day03a(lines): return traverse_map(lines, 0, 0, 1, 3)

def day03b(lines): return math.prod(traverse_map(lines, 0, 0, dy, dx)
                                    for (dy, dx) in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])

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

def test_03_ex1(): assert day03a(ex) == 7
def test_03_ex2(): assert day03b(ex) == 336

def test_03a(day03_lines): assert day03a(day03_lines) == 171
def test_03b(day03_lines): assert day03b(day03_lines) == 1206576000
