def parse(text):
    return [dict(field.split(':', maxsplit=2) for field in passport.split())
            for passport in text.split('\n\n')]

def is_valid(passport):
    return {*passport} >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def is_correct(passport):
    rules = {'byr': lambda x: 1920 <= int(x) <= 2002,
             'iyr': lambda x: 2010 <= int(x) <= 2020,
             'eyr': lambda x: 2020 <= int(x) <= 2030,
             'hgt': lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193)
                           or (x.endswith('in') and  59 <= int(x[:-2]) <=  76),
             'hcl': lambda x: len(x) == 7
                          and x[0] == '#'
                          and all(ch.isdigit() or 'a' <= ch <= 'f' for ch in x[1:]),
             'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
             'pid': lambda x: len(x) == 9
                          and x.isdigit(),
             'cid': lambda _: True}
    return all(rules[k](v) for k, v in passport.items())

def day04a(passports): return sum(is_valid(p) for p in passports)

def day04b(passports): return sum(is_valid(p) and is_correct(p) for p in passports)

def test_04_parse1(): assert len(parse(ex1)) == 4
def test_04_parse2(): assert len(parse(ex1)[0]) == 8

def test_04_ex1(): assert day04a(parse(ex1)) == 2
def test_04_ex2(): assert day04b(parse(ex2)) == 0
def test_04_ex3(): assert day04b(parse(ex3)) == 4

def test_04a(day04_text): assert day04a(parse(day04_text)) == 264
def test_04b(day04_text): assert day04b(parse(day04_text)) == 224

ex1 = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

ex2 = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

ex3 = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''
