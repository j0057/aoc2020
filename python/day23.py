def parse(text):
    return [int(x) for x in text.strip()]

def out(cups, cur):
    s = []
    while cur not in s:
        s.append(cur)
        cur = cups[cur]
    return s

def play(cups, moves):
    cur = cups[0]
    cups = dict(zip(cups, cups[1:] + [cups[0]]))
    highest = max(cups)

    for _ in range(1, moves+1):
        # pick up next 3 cups
        pickup = [cups[cur], cups[cups[cur]], cups[cups[cups[cur]]]]

        # remove them from the circle
        cups[cur] = cups[pickup[-1]]

        # select destination cup: cur-1, wrap around to highest and skip those picked up
        dest = cur-1 if cur>1 else highest
        while dest in pickup:
            dest = dest-1 if dest>1 else highest

        # insert picked up cups back in circle
        cups[pickup[-1]] = cups[dest]
        cups[dest] = pickup[0]

        # select new current cup
        cur = cups[cur]

    return cups

def day23a(cups, moves):
    cups = play(cups, moves)
    return ''.join(map(str, out(cups, 1)))[1:]

def day23b(cups, moves):
    cups.extend(range(10, 1_000_000+1))
    print(len(cups))
    cups = play(cups, moves)
    print(cups[1])
    print(cups[cups[1]])
    return cups[1] * cups[cups[1]]

def test_23_ex1(): assert day23a(parse('389125467'), 10)  == '92658374'
def test_23_ex2(): assert day23a(parse('389125467'), 100) == '67384529'

def test_23a(day23_text): assert day23a(parse(day23_text), 100) == '25368479'

def test_23_ex3(): assert day23b(parse('389125467'), 10_000_000) == 149245887792

def test_23b(day23_text): assert day23b(parse(day23_text), 10_000_000) == 44541319250
