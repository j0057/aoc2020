from functools import reduce

def day14a(program):
    m1, m0, d = reduce(lambda state, line: (int(line[1].replace('X', '0'), 2), int(line[1].replace('X', '1'), 2), state[2])
                                           if line[0] == 'mask'
                                           else (state[0], state[1], {**state[2], **{int(line[0][4:-1]): (int(line[1]) | state[0]) & state[1]}}),
                      [line.split(' = ') for line in program],
                      (0, 0, {}))
    return sum(d.values())

def day14b(program):
    def update(bits, addr, value):
        return {addr: value} if not bits else {**update(bits[1:], addr & (0xfffffffff ^ (1 << bits[0])), value),
                                               **update(bits[1:], addr | (0x000000000 ^ (1 << bits[0])), value)}
    m, f, d = reduce(lambda state, line: (int(line[1].replace('X', '0'), 2), [i for (i, ch) in enumerate(reversed(line[1])) if ch == 'X'], state[2])
                                         if line[0] == 'mask'
                                         else (state[0], state[1], {**state[2], **update(state[1], int(line[0][4:-1]) | state[0], int(line[1]))}),
                     [line.split(' = ') for line in program],
                     (0, [], {}))
    return sum(d.values())

def test_14_ex1(): assert day14a(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
                                  'mem[8] = 11',
                                  'mem[7] = 101',
                                  'mem[8] = 0']) == 165

def test_14_ex2(): assert day14b(['mask = 000000000000000000000000000000X1001X',
                                  'mem[42] = 100',
                                  'mask = 00000000000000000000000000000000X0XX',
                                  'mem[26] = 1']) == 208

def test_14a(day14_lines): assert day14a(day14_lines) == 6513443633260
def test_14b(day14_lines): assert day14b(day14_lines) == 3442819875191
