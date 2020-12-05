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
    row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
    return row, col


def get_id(row: int, col: int) -> int:
    return (row * 8) + col


if __name__ == '__main__':
    with open('day_05/input.txt', 'r') as f:
        seats = [seat.strip() for seat in f]
        print(f'Highest seat ID: {part_1(seats)}')
        print(f'Your seat id: {part_2(seats)}')
