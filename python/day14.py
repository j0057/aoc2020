from functools import reduce

def day14a(program):
    m1, m0, d = reduce(lambda state, line: (int(line[1].replace('X', '0'), 2), int(line[1].replace('X', '1'), 2), state[2])
                                           if line[0] == 'mask'
                                           else (state[0], state[1], {**state[2], **{int(line[0][4:-1]): (int(line[1]) | state[0]) & state[1]}}),
                      [line.split(' = ') for line in program],
                      (0, 0, {}))
    return sum(d.values())

def test_14_ex1(): assert day14a(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
                                  'mem[8] = 11',
                                  'mem[7] = 101',
                                  'mem[8] = 0']) == 165

def test_14a(day14_lines): assert day14a(day14_lines) == 6513443633260
