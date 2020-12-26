from typing import Tuple


def part_1(card: int, door: int) -> int:
    card_loop_size = get_loop_size(card)
    private_key = transform(door, card_loop_size)
    return private_key


def get_loop_size(public_key: int) -> int:
    current, subject = 1, 7
    loops = 0
    while current != public_key:
        current = (current * subject) % 20201227
        loops += 1
    return loops


def transform(public_key: int, loop_size: int) -> int:
    current = 1
    subject = public_key
    for _ in range(loop_size):
        current = (current * subject) % 20201227
    return current


def part_2():
    pass


def parse(filename: str) -> Tuple[int, int]:
    with open(filename, 'r') as f:
        return tuple(int(line.strip()) for line in f)


if __name__ == '__main__':
    card, door = parse('day_25/input.txt')
    print(f'Private key: {part_1(card, door)}')
