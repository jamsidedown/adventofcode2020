from typing import List, Tuple


COMPASS = ['E', 'S', 'W', 'N']


def part_1(directions: List[str]) -> int:
    compass = 0
    x, y, = 0, 0
    for direction in directions:
        bearing, amount = direction[0], int(direction[1:])
        if bearing == 'F':
            bearing = COMPASS[compass % 4]
        elif bearing == 'L':
            compass -= amount // 90
        elif bearing == 'R':
            compass += amount // 90

        if bearing == 'E':
            x += amount
        elif bearing == 'W':
            x -= amount
        elif bearing == 'N':
            y += amount
        elif bearing == 'S':
            y -= amount

    return abs(x) + abs(y)


def part_2(actions: List[str]) -> int:
    x, y = 0, 0
    dx, dy = 10, 1

    for action in actions:
        direction, amount = action[0], int(action[1:])
        if direction == 'F':
            x += dx * amount
            y += dy * amount
        elif direction == 'L':
            dx, dy = rotate(dx, dy, -amount)
        elif direction == 'R':
            dx, dy = rotate(dx, dy, amount)
        elif direction == 'N':
            dy += amount
        elif direction == 'S':
            dy -= amount
        elif direction == 'E':
            dx += amount
        elif direction == 'W':
            dx -= amount

    return abs(x) + abs(y)


def rotate(dx: int, dy: int, angle: int) -> Tuple[int, int]:
    rotations = (angle // 90) % 4

    for _ in range(rotations):
        dx, dy = dy, -dx

    return dx, dy


def parse(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    directions = parse('day_12/input.txt')
    print(f'Manhatten distance for part 1: {part_1(directions)}')
    print(f'Manhatten distance for part 2: {part_2(directions)}')
