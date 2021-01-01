def parse(text):
    p1, p2 = text.split('\n\n')
    return (tuple(int(x) for x in p1.split('\n')[1:]),
            tuple(int(x) for x in p2.split('\n')[1:]))

def crab_combat(D1, D2, R=0):
    seen = set()
    while D1 and D2:
        if (D1, D2) in seen:
            return (True, False)
        seen.add((D1, D2))
        c1, D1 = D1[0], D1[1:]
        c2, D2 = D2[0], D2[1:]
        if R and c1 <= len(D1) and c2 <= len(D2):
            D1, D2 = (D1 + (c1, c2), D2) if crab_combat(D1[:c1], D2[:c2], R)[0] else (D1, D2 + (c2, c1))
            continue
        D1, D2 = (D1 + (c1, c2), D2) if c1 > c2 else (D1, D2 + (c2, c1))
    return (D1, D2)

def score(D1, D2):
    return sum((i+1) * v for d in [D1, D2] for (i, v) in enumerate(reversed(d)))

def day22a(d1, d2):
    return score(*crab_combat(d1, d2))

def day22b(d1, d2):
    return score(*crab_combat(d1, d2, 1))

def test_22_ex1():
    assert day22a(*parse(EX1)) == 306

def test_22_ex2():
    assert day22b(*parse(EX1)) == 291

def test_22a(day22_text):
    assert day22a(*parse(day22_text)) == 33393

def test_22b(day22_text):
    assert day22b(*parse(day22_text)) == 31963

EX1 = 'Player 1:|9|2|6|3|1||Player 2:|5|8|4|7|10'.replace('|', '\n')
