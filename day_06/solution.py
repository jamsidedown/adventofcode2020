from functools import reduce
from operator import iand, ior
from typing import List


def part_1(groups: List[List[str]]) -> int:
    return sum(len(reduce(ior, map(set, group))) for group in groups)


def part_2(groups: List[List[str]]) -> int:
    return sum(len(reduce(iand, map(set, group))) for group in groups)


def parse(filename: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        return [group.splitlines() for group in f.read().split('\n\n')]


if __name__ == '__main__':
    groups = parse('day_06/input.txt')
    print(f'Sum of combined answer counts: {part_1(groups)}')
    print(f'Sum of shared answer counts: {part_2(groups)}')
