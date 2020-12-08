from day_08.solution import parse, part_1, part_2


def test_part_1():
    instructions = parse('day_08/test_input.txt')
    assert part_1(instructions) == 5


def test_part_2():
    instructions = parse('day_08/test_input.txt')
    assert part_2(instructions) == 8
