from typing import List, Set


def part_1(filename: str) -> int:
    with open(filename, 'r') as f:
        parsed = []
        for group in f.read().split('\n\n'):
            group_answers = set()
            for person in group.splitlines():
                answers = set(person.strip())
                group_answers |= answers
            parsed.append(group_answers)

    return sum(len(group) for group in parsed)


def part_2(filename: str) -> int:
    with open(filename, 'r') as f:
        parsed = []
        for group in f.read().split('\n\n'):
            group_answers = set()
            for i, person in enumerate(group.splitlines()):
                answers = set(person.strip())
                if i == 0:
                    group_answers = answers
                group_answers &= answers
            parsed.append(group_answers)

    return sum(len(group) for group in parsed)


if __name__ == '__main__':
    p1 = part_1('day_06/input.txt')
    print(f'Sum of combined answer counts: {p1}')
    p2 = part_2('day_06/input.txt')
    print(f'Sum of shared answer counts: {p2}')
