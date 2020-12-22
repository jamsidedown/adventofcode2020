from day_22.solution import parse, part_1, part_2


def test_part_1():
    player_1, player_2 = parse('day_22/test_input.txt')
    assert part_1(player_1, player_2) == 306


def test_part_2():
    player_1, player_2 = parse('day_22/test_input.txt')
    assert part_2(player_1, player_2) == 291


def test_part_2_recursive_ends():
    player_1, player_2 = parse('day_22/test_input_2.txt')
    assert part_2(player_1, player_2) > 0