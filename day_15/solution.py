from typing import List


def part_1(input: List[int]) -> int:
    return nth_number(input, 2020)


def part_2(input: List[int]) -> int:
    return nth_number(input, 30_000_000)


def nth_number(input: List[int], n: int) -> int:
    spoken = {value: index for index, value in enumerate(input)}
    last = 0

    for index in range(len(input), n - 1):
        last_index = spoken.get(last, index)
        spoken[last] = index
        last = index - last_index

    return last


if __name__ == '__main__':
    input = [0, 1, 4, 13, 15, 12, 16]
    print(f'2020th number spoken: {part_1(input)}')
    print(f'30 millionth number spoken: {part_2(input)}')
