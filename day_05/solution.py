from typing import List, Tuple


def part_1(seats: List[str]) -> int:
    return max(map(parse_seat, seats))


def part_2(seats: List[str]) -> int:
    sids = set(map(parse_seat, seats))
    return next(i for i in range(1024) if i not in sids and (i - 1) in sids and (i + 1) in sids)


def parse_seat(seat: str) -> int:
    bin_vals = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    return int(''.join(map(bin_vals.get, seat)), 2)


if __name__ == '__main__':
    with open('day_05/input.txt', 'r') as f:
        seats = [seat.strip() for seat in f]
        print(f'Highest seat id: {part_1(seats)}')
        print(f'Your seat id: {part_2(seats)}')
