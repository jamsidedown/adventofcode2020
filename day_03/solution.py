from math import prod
from typing import List


def part_1(trees: List[List[int]], dx: int = 3, dy: int = 1) -> int:
    x, y, tree_count = 0, 0, 0
    height, width = len(trees), len(trees[0])

    while y < height:
        tree_count += trees[y][x % width]
        x += dx
        y += dy

    return tree_count


def part_2(trees: List[List[int]]) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = [part_1(trees, dx, dy) for dx, dy in slopes]
    return prod(tree_counts)


def parse(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        values = {'#': 1, '.': 0}
        return [[values[char] for char in line if char in values] for line in f]


if __name__ == '__main__':
    trees = parse('day_03/input.txt')
    print(f'Number of trees in path: {part_1(trees)}')
    print(f'Product of trees in paths: {part_2(trees)}')
