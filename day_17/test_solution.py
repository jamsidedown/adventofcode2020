from day_17.solution import parse, part_1, part_2


def test_part_1():
    cubes = parse('day_17/test_input.txt')
    assert part_1(cubes) == 112


def test_part_2():
    cubes = parse('day_17/test_input.txt')
    assert part_2(cubes) == 848
