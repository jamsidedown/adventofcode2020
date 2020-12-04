import re
from typing import Callable, Dict, List


REQ = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
COLOUR = re.compile(r'^#[\da-f]{6}$')
EYES = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
PID = re.compile(r'^\d{9}$')


PREDICATES: Dict[str, Callable[[str], bool]] = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: parse_height(x),
        'hcl': lambda x: bool(COLOUR.match(x)),
        'ecl': lambda x: x in EYES,
        'pid': lambda x: bool(PID.match(x))
    }



def part_1(passports: List[Dict[str, str]]) -> int:
    valid = 0
    for passport in passports:
        valid += int(all(field in passport for field in REQ))
    return valid


def part_2(passports: List[Dict[str, str]]) -> int:
    valid = 0
    for passport in passports:
        valid += int(all(field in passport and PREDICATES[field](passport[field]) for field in PREDICATES))
    return valid


def parse_height(height: str) -> bool:
    if len(height) < 3:
        return False

    value = int(height[:-2])
    units = height[-2:]

    if units == 'cm':
        return 150 <= value <= 193

    if units == 'in':
        return 59 <= value <= 76

    return False


def parse(filename: str) -> List[Dict[str, str]]:
    passports = []

    with open (filename, 'r') as f:
        for passport in f.read().split('\n\n'):
            parsed = {}
            for field in passport.split():
                key, value = field.split(':')
                parsed[key] = value
            passports.append(parsed)

    return passports


if __name__ == '__main__':
    passports = parse('day_04/input.txt')
    print(f'Number of valid passports (p1): {part_1(passports)}')
    print(f'Number of valid passports (p2): {part_2(passports)}')
