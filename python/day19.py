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

def day19b(grammar, lines):
    grammar.update({8: [[42], [42, 8]], 11: [[42, 31], [42, 11, 31]]})
    return day19a(grammar, lines)

def test_19_ex1():
    assert day19a(*parse(EX1)) == 2

def test_19_ex2():
    assert day19b(*parse(EX2)) == 12

def test_19a(day19_text):
    assert day19a(*parse(day19_text)) == 124

def test_19b(day19_text):
    assert day19b(*parse(day19_text)) == 228

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

EX2 = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''
