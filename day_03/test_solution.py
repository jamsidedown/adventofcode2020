from day_03.solution import parse, part_1, part_2


def test_part_1():
    trees = parse('day_03/test_input.txt')
    assert part_1(trees) == 7


def test_part_2():
    trees = parse('day_03/test_input.txt')
    assert part_2(trees) == 336
