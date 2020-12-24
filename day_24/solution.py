import re
from typing import Dict, List, Tuple


direction_pattern = re.compile(r'[ns]?[ew]')

steps = {
    'e': (2, 0),
    'w': (-2, 0),
    'ne': (1, 1),
    'se': (1, -1),
    'nw': (-1, 1),
    'sw': (-1, -1)
}


def part_1(input: List[str]) -> int:
    tiles = parse_tiles(input)
    return sum(value % 2 for value in tiles.values())


def part_2(input: List[str], iterations: int) -> int:
    tiles = {k: 1 for k, v in parse_tiles(input).items() if v % 2}
    for _ in range(iterations):
        new_tiles = {}
        xs = {x for x, _ in tiles.keys()}
        ys = {y for _, y in tiles.keys()}
        max_x, min_x = max(xs) + 1, min(xs) - 1
        max_y, min_y = max(ys) + 1, min(ys) - 1

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                neighbours = 0
                for sx, sy in steps.values():
                    coords = x + sx, y + sy
                    if coords in tiles:
                        neighbours += tiles[coords] % 2

                if (x, y) in tiles:
                    if 0 < neighbours < 3:
                        new_tiles[(x, y)] = 1
                elif neighbours == 2:
                    new_tiles[(x, y)] = 1
        tiles = new_tiles
    return len(tiles)


def parse_tiles(input: List[str]) -> Dict[str, int]:
    tiles: Dict[str, int] = {}
    for line in input:
        coords = parse(line)
        tiles[coords] = tiles.get(coords, 0) + 1
    return tiles


def parse(directions: str) -> Tuple[int, int]:
    x, y, = 0, 0
    for match in direction_pattern.findall(directions):
        dx, dy = steps.get(match, (0, 0))
        x += dx
        y += dy
    return x, y


def read(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    lines = read('day_24/input.txt')
    print(f'Number of black tiles: {part_1(lines)}')
    print(f'Number of black tiles after 100 days: {part_2(lines, 100)}')
