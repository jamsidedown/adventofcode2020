import re
from typing import List


brackets_pattern = re.compile(r'(\(\d+( [\+\*] \d+)+\))')
sub_pattern = re.compile(r'^\(?(\d+) ([\+\*]) (\d+)\)?')
add_pattern = re.compile(r'\(?(\d+) \+ (\d+)\)?')
mul_pattern = re.compile(r'\(?(\d+) \* (\d+)\)?')


def part_1(equations: List[str]) -> int:
    return sum(calculate_brackets(eq) for eq in equations)


def calculate_brackets(equation: str, advanced: bool = False) -> int:
    calc = calculate_advanced if advanced else calculate
    while '(' in equation:
        match = brackets_pattern.search(equation).group()
        value = calc(match)
        equation = equation.replace(match, value, 1)
    value = calc(equation)
    return int(value)


def calculate(equation: str) -> str:
    while '*' in equation or '+' in equation:
        match = sub_pattern.match(equation)
        first, op, second = match.groups()
        if op == '*':
            value = int(first) * int(second)
        else:
            value = int(first) + int(second)
        equation = equation.replace(match.group(), str(value), 1)
    return equation


def calculate_advanced(equation: str) -> str:
    while '+' in equation:
        match = add_pattern.search(equation)
        first, second = match.groups()
        value = int(first) + int(second)
        equation = equation.replace(match.group(), str(value), 1)
    while '*' in equation:
        match = mul_pattern.search(equation)
        first, second = match.groups()
        value = int(first) * int(second)
        equation = equation.replace(match.group(), str(value), 1)
    return equation


def part_2(equations: List[str]) -> int:
    return sum(calculate_brackets(eq, True) for eq in equations)


if __name__ == '__main__':
    with open('day_18/input.txt', 'r') as f:
        equations = [line.strip() for line in f if line]
        print(f'Sum of maths equations: {part_1(equations)}')
        print(f'Sum of advanced maths equations: {part_2(equations)}')
