from typing import List


def part_1(chairs: List[List[int]]) -> int:
    occupied = [[0 for _ in range(len(chairs[0]))] for _ in range(len(chairs))]
    steps = 0
    while True:
        new_occupied = part_1_step(chairs, occupied)
        steps += 1
        if new_occupied == occupied:
            print(f'{steps} steps')
            return sum(sum(row) for row in new_occupied)
        occupied = new_occupied


def part_1_step(chairs: List[List[int]], occupied: List[List[int]]) -> List[List[int]]:
    new_occupied = []
    height, width = len(chairs), len(chairs[0])

    for y in range(height):
        new_row = []
        for x in range(width):
            if not chairs[y][x]:
                new_row.append(0)
                continue

            seat = occupied[y][x]

            neighbours = part_1_neighbour_count(occupied, y, x)
            if seat:
                new_row.append(int(neighbours < 4))
            else:
                new_row.append(int(neighbours == 0))

        new_occupied.append(new_row)

    return new_occupied


def part_1_neighbour_count(chairs: List[List[int]], row: int, col: int) -> int:
    count = 0
    for y in range(max(row - 1, 0), min(row + 2, len(chairs))):
        for x in range(max(col - 1, 0), min(col + 2, len(chairs[0]))):
            if x == col and y == row:
                continue
            count += chairs[y][x]
    return count


def part_2(chairs: List[List[int]]) -> int:
    occupied = [[0 for _ in range(len(chairs[0]))] for _ in range(len(chairs))]
    steps = 0
    while True:
        new_occupied = part_2_step(chairs, occupied)
        steps += 1
        if new_occupied == occupied:
            print(f'{steps} steps')
            return sum(sum(row) for row in new_occupied)
        occupied = new_occupied


def part_2_step(chairs: List[List[int]], occupied: List[List[int]]) -> List[List[int]]:
    new_occupied = []
    height, width = len(chairs), len(chairs[0])

    for y in range(height):
        new_row = []
        for x in range(width):
            if not chairs[y][x]:
                new_row.append(0)
                continue

            seat = occupied[y][x]

            neighbours = part_2_neighbour_count(chairs, occupied, y, x)
            if seat:
                new_row.append(int(neighbours < 5))
            else:
                new_row.append(int(neighbours == 0))

        new_occupied.append(new_row)

    return new_occupied


def part_2_neighbour_count(chairs: List[List[int]], occupied: List[List[int]], row: int, col: int) -> int:
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue

            y = row + dy
            x = col + dx
            while 0 <= y < len(chairs) and 0 <= x < len(chairs[0]):
                if chairs[y][x]:
                    count += occupied[y][x]
                    break
                y += dy
                x += dx
    return count


def pprint(chairs: List[List[int]], occupied: List[List[int]]) -> None:
    for y in range(len(chairs)):
        line = ''
        for x in range(len(chairs[0])):
            if not chairs[y][x]:
                line += '.'
            elif occupied[y][x]:
                line += '#'
            else:
                line += 'L'
        print(line)
    print('')


def parse(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        return [[int(char == 'L' or char == '#') for char in line.strip()] for line in f]


if __name__ == '__main__':
    chairs = parse('day_11/input.txt')
    print(f'Occupied seats once settled: {part_1(chairs)}')
    print(f'Occupied seats once resettled: {part_2(chairs)}')
