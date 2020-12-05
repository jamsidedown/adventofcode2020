from typing import List, Tuple


def part_1(seats: List[str]) -> int:
    return max(get_id(row, col) for row, col in map(parse_seat, seats))


def part_2(seats: List[str]) -> int:
    seat_ids = {get_id(row, col) for row, col in map(parse_seat, seats)}
    for i in range(get_id(127, 7)):
        if i not in seat_ids:
            if (i - 1) in seat_ids and (i + 1) in seat_ids:
                return i
    return 0


def parse_seat(seat: str) -> Tuple[int, int]:
    row_min, row_max = 0, 127
    col_min, col_max = 0, 7

    for row_char in seat[:7]:
        if row_char == 'F':
            row_max = (row_min + row_max) // 2
        elif row_char == 'B':
            row_min = ((row_min + row_max) // 2) + 1

    for col_char in seat[7:]:
        if col_char == 'L':
            col_max = (col_min + col_max) // 2
        elif col_char == 'R':
            col_min = ((col_min + col_max) // 2) + 1

    assert row_min == row_max
    assert col_min == col_max

    return row_min, col_min


def get_id(row: int, col: int) -> int:
    return (row * 8) + col


if __name__ == '__main__':
    with open('day_05/input.txt', 'r') as f:
        seats = f.readlines()
        print(f'Highest seat ID: {part_1(seats)}')
        print(f'Your seat id: {part_2(seats)}')
