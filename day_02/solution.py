import re
from typing import Callable, List, Tuple


PARSER = re.compile(r'^(\d+)-(\d+) (\w): (\w+)$')


def part_1(passwords: List[str]) -> int:
    valid = 0

    for pw in passwords:
        if match := PARSER.match(pw):
            low, high, char, text = match.groups()
            low, high = int(low), int(high)
            valid += int(low <= text.count(char) <= high)

    return valid


def part_2(passwords: List[str]) -> int:
    valid = 0

    for pw in passwords:
        if match := PARSER.match(pw):
            first, second, char, text = match.groups()
            first, second = int(first) - 1, int(second) - 1
            valid += int((text[first] == char) ^ (text[second] == char))

    return valid


if __name__ == '__main__':
    with open('day_02/input.txt', 'r') as f:
        passwords = f.readlines()
        print(f'Number of valid passwords (policy 1): {part_1(passwords)}')
        print(f'Number of valid passwords (policy 2): {part_2(passwords)}')
