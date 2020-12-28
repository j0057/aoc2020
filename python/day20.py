from functools import reduce
from math import inf

rot = lambda grid: [[grid[y][x] for y in range(len(grid)-1, 0-1, -1)] for x in range(0, len(grid), 1)]
mir = lambda grid: [row[:] for row in reversed(grid)]

bbox = lambda seq: reduce(lambda a, b: (min(a[0], b.imag), max(a[1], b.imag), min(a[2], b.real), max(a[3], b.real)), seq, (+inf, -inf, +inf, -inf))

def parse(text):
    def parse_tiles(tiles):
        for tile in tiles:
            (id, *squares) = tile.split('\n')
            yield (int(id[5:-1]), [[int(sq == '#') for sq in line] for line in squares])
    return {k: [v, rot(v), rot(rot(v)), rot(rot(rot(v))), mir(v), rot(mir(v)), rot(rot(mir(v))), rot(rot(rot(mir(v))))]
            for (k, v) in parse_tiles(text.split('\n\n'))}

def edge_index(tiles):
    T = lambda tile: sum(2**i * v    for (i, v) in enumerate(tile[0]))
    R = lambda tile: sum(2**i * r[9] for (i, r) in enumerate(tile))
    B = lambda tile: sum(2**i * v    for (i, v) in enumerate(tile[9]))
    L = lambda tile: sum(2**i * r[0] for (i, r) in enumerate(tile))
    edges = {k: [{-1j: T(v), 1: R(v), 1j: B(v), -1: L(v)} for v in V]
             for (k, V) in tiles.items()}
    return edges

def walk_edge(grid):
    return {new for cur in grid
                for new in [cur-1j, cur+1, cur+1j, cur-1]
                if new not in grid}

def solve(tiles):                   # --> {tile_id: [grid0, grid90, grid180, grid270, mirrored, mirrored90, mirrored180, mirrored270]}
    edge = edge_index(tiles)        # --> {tile_id: [{-1j:e, 1:e, 1j:e, -1:e} for each of the 8 orientations of a tile]}
    grid = {0: next(iter(tiles))}   # --> {grid_pos: tile_id}
    used = {grid[0]: 0}             # --> {tile_id: orientation}
    while len(grid) < len(tiles):
        remain = {*edge} - {*used}
        for cur in walk_edge(grid):
            t, o = next(((tile, o)
                         for tile in tiles if tile not in used
                         for o in range(8)
                         if all(edge[tile][o][adj-cur] == edge[grid[adj]][used[grid[adj]]][cur-adj]
                                for adj in [cur-1j, cur+1, cur+1j, cur-1]
                                if adj in grid)), (None, None))
            if not t:
                continue
            grid[cur] = t
            used[t] = o
    return (grid, used)

def day20a(tiles):
    grid, _ = solve(tiles)
    t, b, l, r = bbox(grid)
    return grid[l + t * 1j] * grid[r + t * 1j] * grid[l + b * 1j] * grid[r + b * 1j]

def test_20_parse():
    assert parse(EX1)[2311][0][0] == [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    assert parse(EX1)[2311][0][1] == [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]

def test_20_ex1():
    assert day20a(parse(EX1)) == 20899048083289

def test_20a(day20_text):
    assert day20a(parse(day20_text)) == 108603771107737

EX1 = r'''
Tile 2311:|..##.#..#.|##..#.....|#...##..#.|####.#...#|##.##.###.|##...#.###|.#.#.#..##|..#....#..|###...#.#.|..###..###|
Tile 1951:|#.##...##.|#.####...#|.....#..##|#...######|.##.#....#|.###.#####|###.##.##.|.###....#.|..#.#..#.#|#...##.#..|
Tile 1171:|####...##.|#..##.#..#|##.#..#.#.|.###.####.|..###.####|.##....##.|.#...####.|#.##.####.|####..#...|.....##...|
Tile 1427:|###.##.#..|.#..#.##..|.#.##.#..#|#.#.#.##.#|....#...##|...##..##.|...#.#####|.#.####.#.|..#..###.#|..##.#..#.|
Tile 1489:|##.#.#....|..##...#..|.##..##...|..#...#...|#####...#.|#..#.#.#.#|...#.#.#..|##.#...##.|..##.##.##|###.##.#..|
Tile 2473:|#....####.|#..#.##...|#.##..#...|######.#.#|.#...#.#.#|.#########|.###.#..#.|########.#|##...##.#.|..###.#.#.|
Tile 2971:|..#.#....#|#...###...|#.#.###...|##.##..#..|.#####..##|.#..####.#|#..#.#..#.|..####.###|..#.#.###.|...#.#.#.#|
Tile 2729:|...#.#.#.#|####.#....|..#.#.....|....#..#.#|.##..##.#.|.#.####...|####.#.#..|##.####...|##..#.##..|#.##...##.|
Tile 3079:|#.#.#####.|.#..######|..#.......|######....|####.#..#.|.#...#.##.|#.#####.##|..#.###...|..#.......|..#.###...
'''[1:-1].replace('|', '\n')
