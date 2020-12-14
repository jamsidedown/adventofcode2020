import re
from typing import List


mask_pattern = re.compile(r'^mask = ([X01]{36})$')
mem_pattern = re.compile(r'^mem\[(\d+)\] = (\d+)$')


def part_1(instructions: List[str]):
    mem = {}
    or_mask, and_mask = 0, 0

    for instr in instructions:
        if match := mask_pattern.match(instr):
            mask = match.groups()[0]
            or_mask = int(mask.replace('X', '0'), 2)
            and_mask = int(mask.replace('X', '1'), 2)
        elif match := mem_pattern.match(instr):
            address, value = match.groups()
            mem[address] = (int(value) | or_mask) & and_mask

    return sum(mem.values())


def part_2(instructions: List[str]) -> int:
    mem = {}
    mask = ''

    for instr in instructions:
        if match := mask_pattern.match(instr):
            mask = match.groups()[0]
        elif match := mem_pattern.match(instr):
            address_base, value = match.groups()
            for address in resolve_address(int(address_base), mask):
                mem[address] = int(value)

    return sum(mem.values())


def resolve_address(address: int, mask: str) -> List[int]:
    address_str = f'{address:b}'
    masked_address = ''.join(
        (address_str[-i] if (i <= len(address_str) and mask[-i] == '0') else mask[-i])
        for i in range(1, len(mask) + 1)
    )[::-1]
    return resolve_mask(masked_address)


def resolve_mask(mask: str) -> List[int]:
    if 'X' not in mask:
        return [int(mask, 2)]
    else:
        index = mask.index('X')
        pre, post = mask[0:index], mask[index + 1:]
        return resolve_mask(pre + '1' + post) + resolve_mask(pre + '0' + post)


def parse(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    instructions = parse('day_14/input.txt')
    print(f'Sum of values in memory v1: {part_1(instructions)}')
    print(f'Sum of values in memory v2: {part_2(instructions)}')
