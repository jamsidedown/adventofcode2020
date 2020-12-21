from day_21.solution import parse, part_1, part_2


def test_part_1():
    foods = parse('day_21/test_input.txt')
    assert part_1(foods) == 5


def test_part_2():
    foods = parse('day_21/test_input.txt')
    assert part_2(foods) == 'mxmxvkd,sqjhc,fvjkl'
