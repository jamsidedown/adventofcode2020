from day_25.solution import part_1, part_2, parse


def test_part_1():
    card, door = parse('day_25/test_input.txt')
    assert card == 5764801
    assert door == 17807724
    assert part_1(card, door) == 14897079