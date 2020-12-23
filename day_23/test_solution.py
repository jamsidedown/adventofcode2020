from day_23.solution import parse, part_1, part_2


def test_part_1():
    cups = parse('389125467')
    assert part_1(cups, 10) == '92658374'
    assert part_1(cups, 100) == '67384529'


# really slow, like 45s on my macbook
# def test_part_2():
#     cups = parse('389125467')
#     assert part_2(cups, 10_000_000) == 149245887792
