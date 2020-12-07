from day_06.solution import part_1, part_2, parse


def test_part_1_input_1():
    groups = parse('day_06/test_input_1.txt')
    assert part_1(groups) == 6


def test_part_1_input_2():
    groups = parse('day_06/test_input_2.txt')
    assert part_1(groups) == 11


def test_part_2_input_2():
    groups = parse('day_06/test_input_2.txt')
    assert part_2(groups) == 6
