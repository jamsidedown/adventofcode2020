from day_09.solution import parse, part_1, part_2, validate


def test_validate_part_1():
    numbers = [35, 20, 15, 25, 47]
    assert validate(numbers, 40) == True


def test_part_1():
    numbers = parse('day_09/test_input.txt')
    assert part_1(numbers, 5) == 127


def test_part_2():
    numbers = parse('day_09/test_input.txt')
    assert part_2(numbers, 127) == 62
