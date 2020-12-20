from day_20.solution import parse, part_1


def test_part_1():
    tiles = parse('day_20/test_input.txt')
    assert part_1(tiles) == 20899048083289