import enum
from math import prod
import re
from typing import Dict, Iterator, List, Tuple, Union


tile_pattern = re.compile(r'^Tile (\d+):((\n[#\.]+)+)$')
bin_transform = {'#': '1', '.': '0'}
dxdys = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

monster_height = 3
monster_width = 20
monster_hashes = 15
monster_patterns = [
    re.compile(r'^.{18}#.$'),
    re.compile(r'^#(.{4}##){3}#$'),
    re.compile(r'^.#(..#){5}.{3}$')
]


class Tile:
    def __init__(self, input: str):
        self.input = input
        match = tile_pattern.match(input)
        tile_id, tile_source, _ = match.groups()
        self.id = int(tile_id)
        self.source = tile_source.strip().splitlines()
        self.neighbours: List['Tile'] = []
        self.fixed = False

    @property
    def cw_edges(self) -> List[int]:
        top = int(''.join(map(bin_transform.get, self.source[0])), 2)
        right = int(''.join(map(bin_transform.get, [line[-1] for line in self.source])), 2)
        bottom = int(''.join(map(bin_transform.get, self.source[-1][::-1])), 2)
        left = int(''.join(map(bin_transform.get, [line[0] for line in self.source[::-1]])), 2)
        return [top, right, bottom, left]

    @property
    def acw_edges(self) -> List[int]:
        return [int(f'{value:010b}'[::-1], 2) for value in self.cw_edges]

    @property
    def all_edges(self) -> List[int]:
        return self.cw_edges + self.acw_edges

    def rotate(self, rotations: int) -> None:
        for _ in range(rotations):
            self.source = [''.join(line[i] for line in self.source[::-1]) for i in range(len(self.source[0]))]

    def flip_horizontal(self) -> None:
        self.source = [line[::-1] for line in self.source]

    def flip_vertical(self) -> None:
        self.source = self.source[::-1]

    def image(self) -> List[str]:
        return [line[1:-1] for line in self.source[1:-1]]

    def matching_edge(self, other: 'Tile') -> int:
        other_edges = set(other.all_edges)
        for i, edge in enumerate(self.cw_edges):
            if edge in other_edges:
                return i
        return -1

    def get_neighbours(self, tiles: List['Tile']) -> None:
        for tile in tiles:
            if tile.id == self.id:
                continue
            if self.matching_edge(tile) >= 0:
                self.neighbours.append(tile)

    @property
    def neighbour_edges(self) -> List[int]:
        return [self.matching_edge(n) for n in self.neighbours]

    def show(self):
        print('\n'.join(self.source))

    def sea_monsters(self) -> Tuple[int, int]:
        count = 0
        for y in range(0, len(self.source) - monster_height):
            lines = self.source[y:y + monster_height]
            for x in range(0, len(lines[0]) - monster_width):
                search_area = [line[x:x + monster_width] for line in lines]
                if all(monster_patterns[i].match(line) for i, line in enumerate(search_area)):
                    count += 1

        waves = sum(line.count('#') for line in self.source) if count > 0 else 0
        return count, waves


def part_1(tiles: List[Tile]) -> int:
    return prod(tile.id for tile in get_corners(tiles))


def get_corners(tiles: List[Tile]) -> Iterator[Tile]:
    for first in tiles:
        first_edges = set(first.all_edges)
        matched_edges = set()
        for second in [t for t in tiles if t.id != first.id]:
            second_edges = set(second.cw_edges)
            matched_edges |= first_edges & second_edges
        if len(matched_edges) == 2:
            yield first


def part_2(tiles: List[Tile]) -> int:
    grid: Dict[Tuple[int, int], Tile] = {}
    top_left = next(get_corners(tiles))

    for tile in tiles:
        tile.get_neighbours(tiles)

    while sorted(top_left.neighbour_edges) != [1, 2]:
        top_left.rotate(1)
    top_left.fixed = True
    grid[(0, 0)] = top_left

    while not all(tile.fixed for tile in tiles):
        for position, tile in grid.items():
            unfixed = [n for n in tile.neighbours if not n.fixed]
            if unfixed:
                for neighbour in unfixed:
                    edge = tile.matching_edge(neighbour)
                    n_edge = neighbour.matching_edge(tile)
                    rotations = ((edge + 2) - n_edge) % 4
                    neighbour.rotate(rotations)
                    if tile.cw_edges[edge] in neighbour.cw_edges:
                        if edge in {0, 2}:
                            neighbour.flip_horizontal()
                        else:
                            neighbour.flip_vertical()
                    x, y = position
                    dx, dy = dxdys[edge]
                    new_position = (x + dx, y + dy)
                    assert new_position not in grid
                    grid[new_position] = neighbour
                    neighbour.fixed = True
                break

    images = {position: tile.image() for position, tile in grid.items()}

    max_x, max_y = 0, 0
    for index in grid:
        x, y = index
        max_x, max_y = max(x, max_x), max(y, max_y)

    full_image = []
    for y in range(max_y + 1):
        image_line = [images[(x, y)] for x in range(max_x + 1)]
        lines = ['' for _ in range(len(image_line[0]))]
        for image in image_line:
            for i, line in enumerate(image):
                lines[i] += line
        full_image += lines

    full_tile = Tile('Tile 1234:\n' + '\n'.join(full_image))

    for _ in range(4):
        monster_count, waves = full_tile.sea_monsters()
        if monster_count > 0:
            return waves - (monster_count * monster_hashes)
        full_tile.rotate(1)

    full_tile.flip_horizontal()

    for _ in range(4):
        monster_count, waves = full_tile.sea_monsters()
        if monster_count > 0:
            return waves - (monster_count * monster_hashes)
        full_tile.rotate(1)

    return 0


def show(tiles: List[str]) -> None:
    print('\n'.join(tiles))


def parse(filename: str) -> List[Tile]:
    with open(filename, 'r') as f:
        return [Tile(t) for t in f.read().strip().split('\n\n')]


if __name__ == '__main__':
    tiles = parse('day_20/input.txt')
    print(f'Product of corner tile ids: {part_1(tiles)}')
    print(f'Sea monster\'s habitat roughness: {part_2(tiles)}')
