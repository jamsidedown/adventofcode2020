from day_07.solution import parse, part_1, part_2


def test_part_1():
    bags = parse('day_07/test_input_1.txt')
    assert part_1(bags) == 4


def test_part_2_input_1():
    bags = parse('day_07/test_input_1.txt')
    assert part_2(bags) == 32


def test_part_2_input_2():
    bags = parse('day_07/test_input_2.txt')
    assert part_2(bags) == 126
