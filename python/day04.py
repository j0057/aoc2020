def parse(text):
    return [dict(field.split(':', maxsplit=2) for field in passport.split())
            for passport in text.split('\n\n')]

def is_valid(passport):
    expected = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return not expected - set(passport)

def day04a(passports): return sum(is_valid(p) for p in passports)

def test_04_parse1(): assert len(parse(ex1)) == 4
def test_04_parse2(): assert len(parse(ex1)[0]) == 8

def test_04_ex1(): assert day04a(parse(ex1)) == 2

def test_04a(day04_text): assert day04a(parse(day04_text)) == 264

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
