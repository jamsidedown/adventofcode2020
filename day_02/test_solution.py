from day_02.solution import part_1, part_2


def test_part_1():
    passwords = [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc'
    ]

    assert part_1(passwords) == 2


def test_part_2():
    passwords = [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc'
    ]

    assert part_2(passwords) == 1
