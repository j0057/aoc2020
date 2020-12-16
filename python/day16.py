def parse(text):
    fields, mine, nearby = text.split('\n\n')
    return ({name: [tuple(map(int, range.split('-'))) for range in ranges.split(' or ')]
             for name, ranges in (line.split(': ') for line in fields.split('\n'))},
            [int(num) for num in mine.split('\n')[1].split(',')],
            [[int(num) for num in line.split(',')] for line in nearby.split('\n')[1:]])

def invalid_values(fields, mine, nearby):
    return (num for ticket in nearby
                for num in ticket
                if not any(lo <= num <= hi for ranges in fields.values() for lo, hi in ranges))

def day16a(fields, mine, nearby):
    return sum(invalid_values(fields, mine, nearby))

def test_16_parse1(): assert parse(ex1)[0] == {'class': [(1, 3), (5, 7)], 'row': [(6, 11), (33, 44)], 'seat': [(13, 40), (45, 50)]}
def test_16_parse2(): assert parse(ex1)[1] == [7, 1, 14]
def test_16_parse3(): assert parse(ex1)[2] == [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]

def test_16_ex1(): assert day16a(*parse(ex1)) == 71

def test_16a(day16_text): assert day16a(*parse(day16_text)) == 26988

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
