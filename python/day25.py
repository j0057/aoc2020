from itertools import count

def find_key(card_pub, door_pub, modulus=20201227):
    card_loop_size = next(n for n in count(1) if pow(7, n, modulus) == card_pub)
    door_loop_size = next(n for n in count(1) if pow(7, n, modulus) == door_pub)
    return pow(door_pub, card_loop_size, modulus)

def test_25_ex1(): assert find_key(5764801, 17807724) == 14897079

def test_25a(day25_numbers): assert find_key(*day25_numbers) == 5414549

def test_25b(): assert 50 == 50
