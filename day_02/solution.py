import re
from typing import List


parser = re.compile(r'^(\d+)-(\d+) (\w): (\w+)$')


def part_1(passwords: List[str]) -> int:
    valid = 0

    for pw in passwords:
        if match := parser.match(pw):
            low, high, char, text = match.groups()
            low, high = int(low), int(high)
            if low <= text.count(char) <= high:
                valid += 1

    return valid


def part_2(passwords: List[str]) -> int:
    valid = 0

    for pw in passwords:
        if match := parser.match(pw):
            first, second, char, text = match.groups()
            first, second = int(first) - 1, int(second) - 1
            if (text[first] == char) ^ (text[second] == char):
                valid += 1

    return valid


if __name__ == '__main__':
    with open('day_02/input.txt', 'r') as f:
        passwords = f.readlines()
        print(f'Number of valid passwords (policy 1): {part_1(passwords)}')
        print(f'Number of valid passwords (policy 2): {part_2(passwords)}')
