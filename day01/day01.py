from itertools import combinations
from math import prod
from typing import List


def part_1(expenses: List[int]) -> int:
    return next(x * (2020 - x) for x in expenses if 2020 - x in set(expenses))


def part_2(expenses: List[int]) -> int:
    return next(prod(c) * (2020 - sum(c)) for c in combinations(expenses, 2) if 2020 - sum(c) in set(expenses))


if __name__ == '__main__':
    with open('day01/input.txt', 'r') as f:
        expenses = [int(line.strip()) for line in f]
        print(f'Product of two values that sum to 2020: {part_1(expenses)}')
        print(f'Product of three values that sum to 2020: {part_2(expenses)}')