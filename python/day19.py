from functools import reduce

def parse(text):
    grammar, lines = text.split('\n\n')
    grammar = {int(k): r.strip('"')
                       if r.startswith('"') and r.endswith('"')
                       else [[int(x) for x in b.split()] for b in r.split(' | ')]
               for (k, r) in (line.split(': ') for line in grammar.split('\n'))}
    return (grammar, lines.split('\n'))

def match(G, s, r, i):
    if i >= len(s):
        return []
    if isinstance(G[r], str):
        return [i+1] if s[i] == G[r] else []
    return [m for B in G[r]
              for m in reduce(lambda bm, sr: [ni for bi in bm
                                                 for ni in match(G, s, sr, bi)], B, [i])]

def day19a(grammar, lines):
    return sum(len(line) in match(grammar, line, 0, 0) for line in lines)


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
