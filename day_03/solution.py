from math import prod
from typing import List


def part_1(trees: List[List[int]], dx: int = 3, dy: int = 1) -> int:
    height, width = len(trees), len(trees[0])
    return sum(trees[y][(dx * i) % width] for i, y in enumerate(range(0, height, dy)))


def part_2(trees: List[List[int]]) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = [part_1(trees, dx, dy) for dx, dy in slopes]
    return prod(tree_counts)


def parse(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        values = {'#': 1, '.': 0}
        return [list(map(values.get, line.strip())) for line in f]


if __name__ == '__main__':
    trees = parse('day_03/input.txt')
    print(f'Number of trees in path: {part_1(trees)}')
    print(f'Product of trees in paths: {part_2(trees)}')
