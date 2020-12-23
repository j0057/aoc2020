from collections import deque

def parse(text):
    return deque(int(x) for x in text.strip())

def play(cups, moves):
    for _ in range(moves):
        cups.rotate(-1)

        pickup = [cups.popleft() for _ in range(3)]

        cur = dest = cups[-1]
        while True:
            dest = dest - 1 if dest >= 2 else 9
            if dest not in pickup:
                break

        while cups[0] != dest:
            cups.rotate(-1)

        cups.rotate(-1)
        cups.extendleft(reversed(pickup))

        while cups[0] != cur:
            cups.rotate(-1)
        cups.rotate(-1)

    return cups

def day23a(cups, moves):
    cups = play(cups, moves)
    while cups[0] != 1:
        cups.rotate(-1)
    cups.popleft()
    return ''.join(str(x) for x in cups)

def day23b(cups):
    cups.extend(range(10, 1_000_000+1))
    cups = play(cups, 10_000_000)
    while cups[0] != 1:
        cups.rotate(-1)
    cups.rotate(-1)
    return cups.popleft() * cups.popleft()

def test_23_ex1(): assert day23a(parse('389125467'), 10)  == '92658374'
def test_23_ex2(): assert day23a(parse('389125467'), 100) == '67384529'

def test_23_ex3(): assert day23b(parse('389125467')) == 149245887792

def test_23a(day23_text): assert day23a(parse(day23_text), 100) == '25368479'
