from day_24.solution import parse, part_1, part_2, read


def test_parse():
    directions = 'esenee'
    assert parse(directions) == (6, 0)


def test_parse_start():
    directions = 'nwwswee'
    assert parse(directions) == (0, 0)


def test_part_1():
    lines = read('day_24/test_input.txt')
    assert part_1(lines) == 10


def test_part_2():
    lines = read('day_24/test_input.txt')
    assert part_2(lines, 100) == 2208
