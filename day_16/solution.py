import re
from typing import Dict, List, Tuple


range_pattern = re.compile(r'^([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)$')


class Range:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def valid(self, input: int) -> bool:
        return self.low <= input <= self.high


class Field:
    def __init__(self, input: str):
        match = range_pattern.match(input)
        name, l1, h1, l2, h2 = match.groups()
        first = Range(int(l1), int(h1))
        second = Range(int(l2), int(h2))
        self.name = name
        self.ranges = [first, second]

    def valid(self, input: int) -> bool:
        return any(r.valid(input) for r in self.ranges)


def part_1(filename: str) -> int:
    fields, _, tickets = parse(filename)
    total_invalid = 0
    for ticket in tickets:
        for field in ticket:
            if not any(f.valid(field) for f in fields):
                total_invalid += field
    return total_invalid


def part_2(filename: str) -> int:
    fields, my_ticket, tickets = parse(filename)
    valid_tickets = [t for t in tickets if all(any(f.valid(field) for f in fields) for field in t)]

    potential_columns: Dict[str, List[int]] = {}
    for i in range(len(my_ticket)):
        for f in fields:
            columns = potential_columns.setdefault(f.name, [])
            if all(f.valid(t[i]) for t in valid_tickets):
                columns.append(i)

    definite_columns = {}

    while potential_columns:
        for field in potential_columns:
            columns = potential_columns[field]
            if len(columns) == 1:
                col = columns[0]
                definite_columns[field] = col
                potential_columns.pop(field)
                for cols in potential_columns.values():
                    if col in cols:
                        cols.remove(col)
                break

    product = 1
    for col in definite_columns:
        if 'departure' in col:
            col_index = definite_columns[col]
            product *= my_ticket[col_index]

    return product


def parse(filename: str) -> Tuple[List[Field], List[int], List[List[int]]]:
    with open(filename, 'r') as f:
        sections = f.read().split('\n\n')
        fields = [Field(line) for line in sections[0].split('\n')]
        my_ticket = [int(x) for x in sections[1].strip().split('\n')[1].split(',')]
        tickets = [[int(x) for x in line.split(',')] for line in sections[2].strip().split('\n')[1:]]
        return fields, my_ticket, tickets


if __name__ == '__main__':
    p1 = part_1('day_16/input.txt')
    print(f'Sum of invalid fields on tickets: {p1}')
    p2 = part_2('day_16/input.txt')
    print(f'Product of fields starting with departure: {p2}')
