from typing import Dict, List


def part_1(input: List[int]) -> int:
    return nth_number(input, 2020)

def part_2(input: List[int]) -> int:
    return nth_number(input, 30_000_000)


def nth_number(input: List[int], n: int) -> int:
    spoken: Dict[int, List[int]] = {0: []}
    last = 0

    for index, value in enumerate(input):
        spoken[value] = [index]
        last = value

    zero = spoken[0]
    history = spoken[last]

    for index in range(len(input), n):
        if len(history) == 1:
            last = 0
            zero.append(index)
            history = zero
        else:
            last = history[-1] - history[-2]
            history = spoken.setdefault(last, [])
            history.append(index)

    return last


if __name__ == '__main__':
    print(f'2020th number spoken: {part_1([0, 1, 4, 13, 15, 12, 16])}')
    print(f'30 millionth number spoken: {part_2([0, 1, 4, 13, 15, 12, 16])}')
