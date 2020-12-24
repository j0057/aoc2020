import re

def generate_monster(G, rule):
    replace = lambda match: generate_monster(G, match.group(0))
    if G[rule].startswith('"') and G[rule].endswith('"'):
        return G[rule].strip('"')
    else:
        return '(' + re.sub(r'\d+', replace, G[rule]) + ')'

def parse(text):
    grammar, lines = text.split('\n\n')
    grammar = {k: v for (k, v) in (line.split(': ') for line in grammar.split('\n'))}
    regex = generate_monster(grammar, '0')
    return (re.compile('^' + regex + '$', re.VERBOSE), lines.split('\n'))

def day19a(regex, lines):
    return sum(regex.match(line) is not None for line in lines)

def test_19_ex1():
    assert day19a(*parse(EX1)) == 2

def test_19a(day19_text):
    assert day19a(*parse(day19_text)) == 124

EX1 = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''
