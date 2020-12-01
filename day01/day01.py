from itertools import combinations
from math import prod
from typing import List


def part_1(expenses: List[int]) -> int:
    diffs = {2020 - x for x in expenses}
    for exp in expenses:
        if exp in diffs:
            return exp * (2020 - exp)

    return 0


def part_1_ol(expenses: List[int]) -> int:
    return next(i * (2020 - i) for i in expenses if i in {2020 - j for j in expenses})


def part_2(expenses: List[int]) -> int:
    diffs = {2020 - x for x in expenses}
    for i in range(len(expenses)):
        first = expenses[i]
        for j in range(i + 1, len(expenses)):
            second = expenses[j]
            if first + second in diffs:
                third = 2020 - (first + second)
                return first * second * third
    return 0


def part_2_ol(expenses: List[int]) -> int:
    return next(prod(c) * (2020 - sum(c)) for c in combinations(expenses, 2) if sum(c) in {2020 - x for x in expenses})


if __name__ == '__main__':
    with open('day01/input.txt', 'r') as f:
        expenses = [int(line.strip()) for line in f]
        print(f'Product of two values that sum to 2020: {part_1(expenses)}')
        print(f'Product of two values that sum to 2020 (one-liner): {part_1_ol(expenses)}')
        print(f'Product of three values that sum to 2020: {part_2(expenses)}')
        print(f'Product of three values that sum to 2020 (one-liner): {part_2_ol(expenses)}')