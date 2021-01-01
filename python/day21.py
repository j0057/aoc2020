from functools import reduce
import operator as op

def parse(lines):
    return [({*ingredients.split(' ')}, {*allergens[:-1].split(', ')})
            for (ingredients, allergens) in (line.split(' (contains ') for line in lines)]

def solve(foods):
    ingredients = reduce(op.or_, (f[0] for f in foods), set())
    allergens   = reduce(op.or_, (f[1] for f in foods), set())

    suspects = {a: reduce(op.and_, (I for (I, A) in foods if a in A), ingredients)
                for a in allergens}

    solution = {}
    while a := next((a for a in suspects if len(suspects[a]) == 1), None):
        i = suspects[a].pop()
        solution[a] = i
        for I in suspects.values():
            I.discard(i)
        del suspects[a]

    return solution

def day21a(foods):
    dangerous = {*solve(foods).values()}
    return sum(i not in dangerous for (I, A) in foods for i in I)

def day21b(foods):
    solution = solve(foods)
    return ','.join(i for (a, i) in sorted(solution.items()))

def test_21_ex1():
    assert day21a(parse(EX1)) == 5

def test_21_ex2():
    assert day21b(parse(EX1)) == 'mxmxvkd,sqjhc,fvjkl'

def test_21a(day21_lines):
    assert day21a(parse(day21_lines)) == 1685

def test_21b(day21_lines):
    assert day21b(parse(day21_lines)) == 'ntft,nhx,kfxr,xmhsbd,rrjb,xzhxj,chbtp,cqvc'

EX1 = ['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
       'trh fvjkl sbzzf mxmxvkd (contains dairy)',
       'sqjhc fvjkl (contains soy)',
       'sqjhc mxmxvkd sbzzf (contains fish)']
