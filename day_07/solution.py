from functools import reduce
from operator import iadd
import re
from typing import Dict, List, Tuple


OUTER = re.compile(r'^([\w\s]+?) bags contain')
INNER = re.compile(r'(\d+) ([\w\s]+?) bag')


def part_1(bags: Dict[str, List[Tuple[str, str]]]) -> int:
    return len(set(part_1_recurse(bags)))


def part_1_recurse(bags: Dict[str, List[Tuple[str, str]]], bag: str = 'shiny gold') -> List[str]:
    return reduce(iadd, [part_1_recurse(bags, key) + [key] for key in bags for _, colour in bags[key] if colour == bag], [])


def part_2(bags: Dict[str, List[Tuple[str, str]]], bag: str = 'shiny gold') -> int:
    return sum(int(count) * (1 + part_2(bags, colour)) for count, colour in bags.get(bag, []))


def parse(filename: str) -> int:
    with open(filename, 'r') as f:
        return {OUTER.match(line).groups()[0]: INNER.findall(line) for line in f}


if __name__ == '__main__':
    bags = parse('day_07/input.txt')
    print(f'Number of bags that can eventually hold a shiny gold bag: {part_1(bags)}')
    print(f'Maximum number of bags within a shiny gold bag: {part_2(bags)}')
