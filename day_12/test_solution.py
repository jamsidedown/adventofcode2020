from day_12.solution import part_1, part_2


def test_part_1():
    directions = ['F10', 'N3', 'F7', 'R90', 'F11']
    assert part_1(directions) == 25


def test_part_2():
    directions = ['F10', 'N3', 'F7', 'R90', 'F11']
    assert part_2(directions) == 286
