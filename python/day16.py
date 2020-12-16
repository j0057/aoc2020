from functools import reduce
from math import prod

def parse(text):
    fields, mine, nearby = text.split('\n\n')
    return ({name: [tuple(map(int, range.split('-'))) for range in ranges.split(' or ')]
             for name, ranges in (line.split(': ') for line in fields.split('\n'))},
            [int(num) for num in mine.split('\n')[1].split(',')],
            [[int(num) for num in line.split(',')] for line in nearby.split('\n')[1:]])

def invalid_values(fields, ticket):
    return [value for value in ticket
                  if not any(lo <= value <= hi for ranges in fields.values() for lo, hi in ranges)]

def field_names(fields, tickets):
    return [reduce(lambda a, b: a & b,
                   ({name for name, ranges in fields.items()
                          if any(lo <= ticket[i] <= hi for lo, hi in ranges)}
                    for ticket in tickets),
                   {*fields})
            for i in range(len(fields))]

def day16a(fields, mine, nearby):
    return sum(value for ticket in nearby
                     for value in invalid_values(fields, ticket))

def day16b(fields, mine, nearby, target):
    names = field_names(fields, [ticket for ticket in nearby if not invalid_values(fields, ticket)])
    uncertain = {*range(len(fields))}
    while name := next((next(iter(n)) for (i, n) in enumerate(names) if len(n) == 1 and i in uncertain), None):
        for (i, possible) in enumerate(names):
            if len(possible) == 1:
                uncertain.discard(i)
            else:
                possible.discard(name)
    return prod(mine[i] for i, name in enumerate(next(iter(n)) for n in names) if name.startswith(target))

def test_16_parse1(): assert parse(ex1)[0] == {'class': [(1, 3), (5, 7)], 'row': [(6, 11), (33, 44)], 'seat': [(13, 40), (45, 50)]}
def test_16_parse2(): assert parse(ex1)[1] == [7, 1, 14]
def test_16_parse3(): assert parse(ex1)[2] == [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]

def test_16_ex1(): assert day16a(*parse(ex1)) == 71
def test_16_ex2(): assert day16b(*parse(ex2), 'class') == 12

def test_16a(day16_text): assert day16a(*parse(day16_text)) == 26988
def test_16b(day16_text): assert day16b(*parse(day16_text), target='departure ') == 426362917709

ex1 = '''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''[1:]

ex2 = '''
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''[1:]
