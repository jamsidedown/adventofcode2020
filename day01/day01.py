from typing import List


def part_1(expenses: List[int]) -> int:
    for i in range(len(expenses)):
        first = expenses[i]
        for j in range(i + 1, len(expenses)):
            second = expenses[j]
            if first + second == 2020:
                return first * second
    return 0


def part_2(expenses: List[int]) -> int:
    for i in range(len(expenses)):
        first = expenses[i]
        for j in range(i + 1, len(expenses)):
            second = expenses[j]
            for k in range(j + 1, len(expenses)):
                third = expenses[k]
                if first + second + third == 2020:
                    return first * second * third
    return 0


if __name__ == '__main__':
    with open('day01/input.txt', 'r') as f:
        expenses = [int(line.strip()) for line in f]
        print(f'Product of two values that sum to 2020: {part_1(expenses)}')
        print(f'Product of three values that sum to 2020: {part_2(expenses)}')