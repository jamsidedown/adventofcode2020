from day_18.solution import part_1, part_2


def test_part_1_example_1():
    assert part_1(['1 + 2 * 3 + 4 * 5 + 6']) == 71


def test_part_1_example_2():
    assert part_1(['1 + (2 * 3) + (4 * (5 + 6))']) == 51


def test_part_1_example_3():
    assert part_1(['2 * 3 + (4 * 5)']) == 26


def test_part_1_example_4():
    assert part_1(['5 + (8 * 3 + 9 + 3 * 4 * 3)']) == 437


def test_part_1_example_5():
    assert part_1(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']) == 12240


def test_part_1_example_6():
    assert part_1(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']) == 13632


def test_part_1_failure_1():
    assert part_1(['7 * 2 + 6 * 7 * (8 + 8 * (7 + 2 + 8) + 8 + 9 * 8)']) == 323680  # not 286240


def test_part_1_failure_2():
    assert part_1(['7 + 2 * 2 + (7 + 9 + 7 * 3) * 2']) == 174  # not 636


def test_part_1_example_1():
    assert part_2(['1 + 2 * 3 + 4 * 5 + 6']) == 231


def test_part_1_example_2():
    assert part_2(['1 + (2 * 3) + (4 * (5 + 6))']) == 51


def test_part_2_example_3():
    assert part_2(['2 * 3 + (4 * 5)']) == 46


def test_part_2_example_4():
    assert part_2(['5 + (8 * 3 + 9 + 3 * 4 * 3)']) == 1445


def test_part_2_example_5():
    assert part_2(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']) == 669060


def test_part_2_example_6():
    assert part_2(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']) == 23340
