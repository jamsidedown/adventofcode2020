from typing import List


class Tile:
    def __init__(self, char: str, x: int, y: int, neighbour_limit: int):
        self.seat = char in {'#', 'L'}
        self.occupied = char == '#'
        self.previously_occupied = self.occupied
        self.x = x
        self.y = y
        self.neighbours: List[Tile] = []
        self.neighbour_limit = neighbour_limit

    @property
    def _occupied_neighbours(self) -> int:
        return sum(seat.previously_occupied for seat in self.neighbours)

    def store(self):
        self.previously_occupied = self.occupied

    def update(self):
        if self.previously_occupied:
            self.occupied = self._occupied_neighbours < self.neighbour_limit
        else:
            self.occupied = self._occupied_neighbours == 0

    @property
    def stable(self):
        return self.occupied == self.previously_occupied

    @property
    def char(self):
        if not self.seat:
            return '.'
        if self.occupied:
            return '#'
        return 'L'


class Grid:
    def __init__(self, seats: List[str], immediate_neighbours: bool, neighbour_limit: int):
        self.seats = [[Tile(char, x, y, neighbour_limit) for x, char in enumerate(row.strip())] for y, row in enumerate(seats)]
        self.height = len(self.seats)
        self.width = len(self.seats[0])
        for row in self.seats:
            for seat in row:
                seat.neighbours = self.neighbours(seat) if immediate_neighbours else self.visible_neighbours(seat)

    def get(self, row: int, col: int) -> Tile:
        return self.seats[row][col]

    def neighbours(self, seat: Tile) -> List[Tile]:
        neighbours = []
        for dy in range(-1, 2):
            y = seat.y + dy
            if y < 0 or y >= self.height:
                continue
            for dx in range(-1, 2):
                x = seat.x + dx
                if x < 0 or x >= self.width:
                    continue
                if dx == 0 and dy == 0:
                    continue
                tile = self.get(y, x)
                if tile.seat:
                    neighbours.append(tile)
        return neighbours

    def visible_neighbours(self, seat: Tile) -> List[Tile]:
        neighbours = []
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue

                y = seat.y + dy
                x = seat.x + dx
                while 0 <= y < self.height and 0 <= x < self.width:
                    tile = self.get(y, x)
                    if tile.seat:
                        neighbours.append(tile)
                        break
                    y += dy
                    x += dx
        return neighbours


    def step(self) -> None:
        for row in self.seats:
            for tile in row:
                if not tile.seat:
                    continue
                tile.update()

    def store(self):
        for row in self.seats:
            for tile in row:
                tile.store()

    @property
    def stable(self) -> bool:
        return all(seat.stable for row in self.seats for seat in row)

    @property
    def total(self):
        return sum(sum(tile.previously_occupied for tile in row) for row in self.seats)

    def pprint(self):
        print('')
        for y in range(self.height):
            print(''.join(self.get(y, x).char for x in range(self.width)))
        print('')

    def run(self):
        while True:
            self.step()
            if self.stable:
                return self.total
            self.store()


def part_1(filename: str) -> int:
    return parse(filename, True, 4).run()


def part_2(filename: str) -> int:
    return parse(filename, False, 5).run()


def parse(filename: str, immediate_neighbours: bool, neighbour_limit: int) -> Grid:
    with open(filename, 'r') as f:
        return Grid(f.readlines(), immediate_neighbours, neighbour_limit)


if __name__ == '__main__':
    p1 = part_1('day_11/input.txt')
    print(f'Occupied seats once settled: {p1}')
    p2 = part_2('day_11/input.txt')
    print(f'Occupied seats once resettled: {p2}')
