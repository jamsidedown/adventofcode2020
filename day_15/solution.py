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

    for index in range(len(input), n):
        history = spoken[last]
        if len(history) == 1:
            last = 0
            spoken[last].append(index)
        else:
            last = history[-1] - history[-2]
            sub = spoken.get(last, [])
            sub.append(index)
            spoken[last] = sub

    return last


if __name__ == '__main__':
    print(f'2020th number spoken: {part_1([0, 1, 4, 13, 15, 12, 16])}')
    print(f'30 millionth number spoken: {part_2([0, 1, 4, 13, 15, 12, 16])}')
