from typing import List


def part_1(numbers: List[int], preamble: int) -> int:
    for i in range(preamble, len(numbers)):
        if not validate(numbers[i - preamble:i], numbers[i]):
            return numbers[i]
    return 0


def validate(sub: List[int], target: int) -> bool:
    return any({target - x for x in sub} & set(sub))


def part_2(numbers: List[int], target: int) -> int:
    start, stop = 0, 1
    while stop < len(numbers):
        cont_nums = numbers[start:stop]
        cont_sum = sum(cont_nums)
        if cont_sum == target:
            return min(cont_nums) + max(cont_nums)
        if cont_sum < target:
            stop += 1
        if cont_sum > target:
            start += 1
    return 0


def parse(filename: str) -> List[int]:
    with open (filename, 'r') as f:
        return [int(line.strip()) for line in f]


if __name__ == '__main__':
    numbers = parse('day_09/input.txt')
    p1 = part_1(numbers, 25)
    print(f'First number that isn\'t the sum of two of the previous 25 numbers: {p1}')
    print(f'Sum of largest and smallest values in a contiguous subset that sum to {p1}: {part_2(numbers, p1)}')
