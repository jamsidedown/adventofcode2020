from functools import lru_cache
from typing import List


def part_1(adapters: List[int]) -> int:
    diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
    return diffs.count(1) * diffs.count(3)


def part_2(adapters: List[int]) -> int:
    @lru_cache
    def recurse(i: int) -> int:
        total = 0
        for j in range(i + 1, len(adapters)):
            if adapters[j] - adapters[i] > 3:
                break
            total += recurse(j)
        return total or 1

    return recurse(0)


def parse(filename: str) -> List[int]:
    with open(filename, 'r') as f:
        adapters = sorted(int(line) for line in f)
        return [0, *adapters, adapters[-1] + 3]


if __name__ == '__main__':
    adapters = parse('day_10/input.txt')
    print(f'Product of one jump and three jump counts: {part_1(adapters)}')
    print(f'Total number of arrangements: {part_2(adapters)}')
