from day_15.solution import part_1, part_2


def test_part_1_input_1():
    assert part_1([0, 3, 6]) == 436


def test_part_1_input_2():
    assert part_1([1, 3, 2]) == 1


def test_part_1_input_3():
    assert part_1([2, 1, 3]) == 10


# really slow to run
# def test_part_2_input_1():
#     assert part_2([0, 3, 6]) == 175594
