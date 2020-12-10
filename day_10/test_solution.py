from day_10.solution import parse, part_1, part_2


def test_part_1_input_1():
    adapters = parse('day_10/test_input_1.txt')
    assert part_1(adapters) == 35


def test_part_1_input_2():
    adapters = parse('day_10/test_input_2.txt')
    assert part_1(adapters) == 220


def test_part_2_input_1():
    adapters = parse('day_10/test_input_1.txt')
    assert part_2(adapters) == 8


def test_part_2_input_2():
    adapters = parse('day_10/test_input_2.txt')
    assert part_2(adapters) == 19208
