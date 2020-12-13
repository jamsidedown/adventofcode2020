from day_13.solution import parse, part_1, part_2, Bus


def test_part_1():
    timestamp, buses = parse('day_13/test_input.txt')
    assert part_1(timestamp, buses) == 295


def test_part_2_example_1():
    buses = list(Bus.parse('17,x,13,19'))
    assert part_2(buses) == 3417

# x % 17 == (x + 2) % 13 == (x + 3) % 19 == 0

# (3417 + 0) % 17 == 0
# 3417 % 17 == 0

# 17x = 13y - 2 = 19z - 3
# x := 201
# y = 263
# z = 180

# (3417 + 2) % 13 == 0
# 3417 % 13 == (13 - 2) % 13

# (3417 + 3) % 19 == 0
# 3417 % 19 == (19 - 3) % 19


def test_part_2_full():
    _, buses = parse('day_13/test_input.txt')
    assert part_2(buses) == 1068781
