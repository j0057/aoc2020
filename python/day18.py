import tatsu

GRAMMAR = tatsu.compile(r'''
    start   = expr $ ;
    expr    = add | mul | term ;
    add     = left:expr op:"+" right:term ;
    mul     = left:expr op:"*" right:term ;
    term    = "(" @:expr ")" | num ;
    num     = /\d+/ ;
''')

class Evaluator(object):
    def num(self, node): return int(node)
    def add(self, node): return node.left + node.right
    def mul(self, node): return node.left * node.right

def day18a(lines): return sum(GRAMMAR.parse(line, semantics=Evaluator()) for line in lines)
def test_18_ex0():  assert day18a(['1 + 2 * 3 + 4 * 5 + 6'])                           == 71
def test_18_ex1():  assert day18a(['1 + (2 * 3) + (4 * (5 + 6))'])                     == 51
def test_18_ex2():  assert day18a(['2 * 3 + (4 * 5)'])                                 == 26
def test_18_ex3():  assert day18a(['5 + (8 * 3 + 9 + 3 * 4 * 3)'])                     == 437
def test_18_ex4():  assert day18a(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'])       == 12240
def test_18_ex5():  assert day18a(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']) == 13632


def test_18a(day18_lines): assert day18a(day18_lines) == 5374004645253
