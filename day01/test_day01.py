from day01.day01 import part_1, part_2


def test_part_1_example():
    expenses = [1721, 979, 366, 299, 675, 1456]
    assert 514579 == part_1(expenses)


def test_part_2_example():
    expenses = [1721, 979, 366, 299, 675, 1456]
    assert 241861950 == part_2(expenses)
