from typing import List


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


def part_2():
    pass


def parse(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    directions = parse('day_12/input.txt')
    print(part_1(directions))
