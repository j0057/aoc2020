import re

def parse(lines):
    for line in lines:
        bag = re.match(r'^(\w+ \w+)', line).group(1)
        if re.match('no other bags.$', line):
            yield (bag, [])
        else:
            contents = [(int(m.group(1)), m.group(2)) for m in re.finditer(r'(\d+) (\w+ \w+) bags?', line)]
            yield (bag, contents)

def find(bags, T):
    def find(c):
        return c == T or any(find(k) for (n, k) in bags[c])
    return sum(find(k) for k in bags if k != T)

def count(bags, c, i=''):
    return 1 + sum(n * count(bags, k) for n,k in bags[c])

def day07a(bags): return find(dict(bags), 'shiny gold')
def day07b(bags): return count(dict(bags), 'shiny gold')-1

def test_07_ex1(): assert day07a(parse(ex1)) == 4
def test_07_ex2(): assert day07b(parse(ex1)) == 32
def test_07_ex3(): assert day07b(parse(ex2)) == 126

def test_07a(day07_lines): assert day07a(parse(day07_lines)) == 287
def test_07b(day07_lines): assert day07b(parse(day07_lines)) == 48160

ex1 = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
       'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
       'bright white bags contain 1 shiny gold bag.',
       'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
       'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
       'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
       'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
       'faded blue bags contain no other bags.',
       'dotted black bags contain no other bags.']

ex2 = ['shiny gold bags contain 2 dark red bags.',
       'dark red bags contain 2 dark orange bags.',
       'dark orange bags contain 2 dark yellow bags.',
       'dark yellow bags contain 2 dark green bags.',
       'dark green bags contain 2 dark blue bags.',
       'dark blue bags contain 2 dark violet bags.',
       'dark violet bags contain no other bags.']
