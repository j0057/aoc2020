import tatsu

GRAMMAR = tatsu.compile(r'''
    start   = expr $ ;
    expr    = add | mul | term ;
    add     = left:expr op:"+" right:term ;
    mul     = left:expr op:"*" right:term ;
    term    = "(" @:expr ")" | num ;
    num     = /\d+/ ;
''')

ADVANCED = tatsu.compile(r'''
    start   = expr $ ;
    expr    = mul | term ;
    mul     = left:expr op:"*" right:term ;
    term    = add | addend ;
    add     = left:term op:"+" right:addend ;
    addend  = "(" @:expr ")" | num ;
    num     = /\d+/ ;
''')

class Evaluator(object):
    def num(self, node): return int(node)
    def add(self, node): return node.left + node.right
    def mul(self, node): return node.left * node.right

def day18a(lines): return sum(GRAMMAR.parse(line, semantics=Evaluator()) for line in lines)
def day18b(lines): return sum(ADVANCED.parse(line, semantics=Evaluator()) for line in lines)

def test_18_ex0():  assert day18a(['1 + 2 * 3 + 4 * 5 + 6'])                           == 71
def test_18_ex1():  assert day18a(['1 + (2 * 3) + (4 * (5 + 6))'])                     == 51
def test_18_ex2():  assert day18a(['2 * 3 + (4 * 5)'])                                 == 26
def test_18_ex3():  assert day18a(['5 + (8 * 3 + 9 + 3 * 4 * 3)'])                     == 437
def test_18_ex4():  assert day18a(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'])       == 12240
def test_18_ex5():  assert day18a(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']) == 13632

def test_18_ex6():  assert day18b(['1 + 2 * 3 + 4 * 5 + 6'])                           == 231
def test_18_ex7():  assert day18b(['1 + (2 * 3) + (4 * (5 + 6))'])                     == 51
def test_18_ex8():  assert day18b(['2 * 3 + (4 * 5)'])                                 == 46
def test_18_ex9():  assert day18b(['5 + (8 * 3 + 9 + 3 * 4 * 3)'])                     == 1445
def test_18_ex10(): assert day18b(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'])       == 669060
def test_18_ex11(): assert day18b(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']) == 23340

def test_18a(day18_lines): assert day18a(day18_lines) == 5374004645253
def test_18b(day18_lines): assert day18b(day18_lines) == 88782789402798
