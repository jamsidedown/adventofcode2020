from day_13.solution import parse, part_1, part_2, Bus


def test_part_1():
    timestamp, buses = parse('day_13/test_input.txt')
    assert part_1(timestamp, buses) == 295


def test_part_2_example_1():
    buses = list(Bus.parse('17,x,13,19'))
    assert part_2(buses) == 3417


def test_part_2_mini_example():
    buses = list(Bus.parse('17,x,13'))
    assert part_2(buses) == 102
    buses = list(Bus.parse('17,19'))
    assert part_2(buses) == 170

# 102 = 0 mod 17
# 102 = 11 mod 13


def test_part_2_full():
    _, buses = parse('day_13/test_input.txt')
    assert part_2(buses) == 1068781
