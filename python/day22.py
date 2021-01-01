
def parse(text):
    p1, p2 = text.split('\n\n')
    return (tuple(int(x) for x in p1.split('\n')[1:]),
            tuple(int(x) for x in p2.split('\n')[1:]))

def crab_combat(D1, D2):
    yield (D1, D2)
    while D1 and D2:
        c1, D1 = D1[0], D1[1:]
        c2, D2 = D2[0], D2[1:]
        D1, D2 = (D1 + (c1, c2), D2) if c1 > c2 else (D1, D2 + (c2, c1))
        yield (D1, D2)

def day22a(d1, d2):
    D = [*crab_combat(d1, d2)]
    return sum((i+1) * v for d in D[-1]
                         for (i, v) in enumerate(reversed(d)))

def test_22_ex1():
    assert day22a(*parse(EX1)) == 306

def test_22a(day22_text):
    assert day22a(*parse(day22_text)) == 33393

EX1 = 'Player 1:|9|2|6|3|1||Player 2:|5|8|4|7|10'.replace('|', '\n')
