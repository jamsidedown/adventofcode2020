from day_05.solution import parse_seat, part_1


def test_parse_seat():
    seat = 'FBFBBFFRLR'
    assert parse_seat(seat) == (44, 5)


def test_parse_seat_567():
    seat = 'BFFFBBFRRR'
    assert parse_seat(seat) == (70, 7)


def test_parse_seat_119():
    seat = 'FFFBBBFRRR'
    assert parse_seat(seat) == (14, 7)


def test_parse_seat_820():
    seat = 'BBFFBBFRLL'
    assert parse_seat(seat) == (102, 4)


def test_part_1():
    seats = [
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL'
    ]
    assert part_1(seats) == 820
