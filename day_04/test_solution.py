from day_04.solution import parse, part_1, part_2, PREDICATES


def test_part_1():
    passports = parse('day_04/test_input.txt')
    assert part_1(passports) == 2


def test_part_2_individual_examples():
    assert PREDICATES['byr']('2002')
    assert not PREDICATES['byr']('2003')

    assert PREDICATES['hgt']('60in')
    assert PREDICATES['hgt']('190cm')
    assert not PREDICATES['hgt']('190in')
    assert not PREDICATES['hgt']('190')

    assert PREDICATES['hcl']('#123abc')
    assert not PREDICATES['hcl']('#123abz')
    assert not PREDICATES['hcl']('123abc')

    assert PREDICATES['ecl']('brn')
    assert not PREDICATES['ecl']('wat')

    assert PREDICATES['pid']('000000001')
    assert not PREDICATES['pid']('0123456789')


def test_invalid_part_2():
    passports = parse('day_04/test_invalid_part_2.txt')
    assert part_2(passports) == 0


def test_valid_part_2():
    passports = parse('day_04/test_valid_part_2.txt')
    assert part_2(passports) == 4
