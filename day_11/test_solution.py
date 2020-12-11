from day_11.solution import parse, part_1_neighbour_count, part_1, part_2, part_2_neighbour_count


def test_parse():
    chairs = parse('day_11/test_input.txt')
    assert chairs[0] == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]


def test_part_1_neighbour_count():
    chairs = parse('day_11/test_input.txt')
    assert part_1_neighbour_count(chairs, 0, 0) == 2
    assert part_1_neighbour_count(chairs, 1, 1) == 6


def test_part_1():
    chairs = parse('day_11/test_input.txt')
    assert part_1(chairs) == 37


def test_part_2():
    chairs = parse('day_11/test_input.txt')
    assert part_2(chairs) == 26


def test_part_2_neighbour_count():
    chairs = parse('day_11/test_input_2.txt')
    assert part_2_neighbour_count(chairs, chairs, 4, 3) == 8


def test_part_2_neighbour_counl_2t():
    chairs = parse('day_11/test_input_3.txt')
    assert part_2_neighbour_count(chairs, chairs, 3, 3) == 0
