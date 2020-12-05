from day_04.solution import parse, part_1, part_2, VALIDATORS


def test_part_1():
    passports = parse('day_04/test_input.txt')
    assert part_1(passports) == 2


def test_part_2_individual_examples():
    assert VALIDATORS['byr']('2002')
    assert not VALIDATORS['byr']('2003')

    assert VALIDATORS['hgt']('60in')
    assert VALIDATORS['hgt']('190cm')
    assert not VALIDATORS['hgt']('190in')
    assert not VALIDATORS['hgt']('190')

    assert VALIDATORS['hcl']('#123abc')
    assert not VALIDATORS['hcl']('#123abz')
    assert not VALIDATORS['hcl']('123abc')

    assert VALIDATORS['ecl']('brn')
    assert not VALIDATORS['ecl']('wat')

    assert VALIDATORS['pid']('000000001')
    assert not VALIDATORS['pid']('0123456789')


def test_invalid_part_2():
    passports = parse('day_04/test_invalid_part_2.txt')
    assert part_2(passports) == 0


def test_valid_part_2():
    passports = parse('day_04/test_valid_part_2.txt')
    assert part_2(passports) == 4
