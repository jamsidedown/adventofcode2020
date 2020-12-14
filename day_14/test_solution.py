from day_14.solution import part_1, parse, part_2


def test_part_1():
    instructions = parse('day_14/test_input.txt')
    assert part_1(instructions) == 165


def test_part_2():
    instructions = parse('day_14/test_input_2.txt')
    assert part_2(instructions) == 208
