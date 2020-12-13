from math import ceil, log, log10, prod, sqrt
from typing import Iterator, List, Tuple, Union


class Bus:
    def __init__(self, id: int, offset: int):
        self.id = id
        self.offset = offset

    @staticmethod
    def parse(input: str) -> Iterator['Bus']:
        for index, value in enumerate(input.split(',')):
            if bus_id := try_int(value):
                yield Bus(bus_id, index)


def part_1(timestamp: int, buses: List[Bus]):
    t = timestamp
    while True:
        for bus in buses:
            if t % bus.id == 0:
                return bus.id * (t - timestamp)
        t += 1


def part_2(buses: List[Bus]) -> int:
    first = buses[0]
    timestamp = 0
    jump = first.id
    offset = 1

    while True:
        timestamp += jump
        for bus in buses[offset:]:
            if (timestamp + bus.offset) % bus.id == 0:
                offset += 1
                jump *= bus.id
                if offset == len(buses):
                    return timestamp
            else:
                break


def parse(filename: str) -> Tuple[int, List[Bus]]:
    with open(filename, 'r') as f:
        lines = f.readlines()
        timestamp = int(lines[0].strip())
        buses = Bus.parse(lines[1].strip())
        return timestamp, list(buses)


def try_int(value: str) -> Union[int, None]:
    try:
        return int(value.strip())
    except:
        return None


if __name__ == '__main__':
    timestamp, buses = parse('day_13/input.txt')
    print(f'Wait in minutes * bus id: {part_1(timestamp, buses)}')
    print(f'First timestamp with offsets: {part_2(buses)}')
