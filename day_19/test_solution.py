from day_19.solution import parse, part_1, part_2


def test_part_1():
    rules, messages = parse('day_19/test_input.txt')
    assert part_1(rules, messages) == 2


def test_part_1_example_2():
    rules, messages = parse('day_19/test_input_2.txt')
    assert part_1(rules, messages) == 3


def test_part_2():
    rules, messages = parse('day_19/test_input_2.txt')
    assert part_2(rules, messages) == 12
