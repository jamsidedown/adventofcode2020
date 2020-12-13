from math import log, log10
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


def part_2_old(buses: List[Bus]) -> int:
    first = buses[0]
    timestamp = 0
    while True:
        timestamp += first.id
        success = True
        for bus in buses[1:]:
            if not (timestamp + bus.offset) % bus.id == 0:
                success = False
                break
        if success:
            return timestamp


def part_2(buses: List[Bus]) -> int:
    buses = sorted(buses, key=lambda b: b.id, reverse=True)

    for bus in buses:
        bus.offset = bus.offset % bus.id

    first = buses[0]
    counter = 1

    ln = 1

    while True:
        timestamp = (first.id * counter) - first.offset
        if new_ln := int(log(timestamp)):
            if new_ln > ln:
                ln = new_ln
                print(new_ln)
        success = True
        for bus in buses[1:]:
            if not (timestamp + bus.offset) % bus.id == 0:
                success = False
                break
        if success:
            return timestamp
        counter += 1


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
