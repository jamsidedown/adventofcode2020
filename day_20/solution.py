import re
from typing import List


tile_pattern = re.compile(r'^Tile (\d+):((\n[#\.]{10}){10})$')
bin_transform = {'#': '1', '.': '0'}


class Tile:
    def __init__(self, input: str):
        self.input = input
        match = tile_pattern.match(input)
        tile_id, tile_source, _ = match.groups()
        self.id = int(tile_id)
        self.source = tile_source.strip().splitlines()

    @property
    def cw_edges(self) -> List[int]:
        top = int(''.join(map(bin_transform.get, self.source[0])), 2)
        right = int(''.join(map(bin_transform.get, [line[-1] for line in self.source])), 2)
        bottom = int(''.join(map(bin_transform.get, self.source[-1][::-1])), 2)
        left = int(''.join(map(bin_transform.get, [line[0] for line in self.source[::-1]])), 2)
        return [top, right, bottom, left]

    @property
    def acw_edges(self) -> List[int]:
        top = int(''.join(map(bin_transform.get, self.source[0][::-1])), 2)
        right = int(''.join(map(bin_transform.get, [line[-1] for line in self.source[::-1]])), 2)
        bottom = int(''.join(map(bin_transform.get, self.source[-1])), 2)
        left = int(''.join(map(bin_transform.get, [line[0] for line in self.source])), 2)
        return [top, right, bottom, left]

    @property
    def all_edges(self) -> List[int]:
        return self.cw_edges + self.acw_edges


def part_1(tiles: List[Tile]) -> int:
    product = 1
    for first in tiles:
        first_edges = set(first.all_edges)
        matched_edges = set()
        for second in [t for t in tiles if t.id != first.id]:
            second_edges = set(second.cw_edges)
            matched_edges |= first_edges & second_edges
        if len(matched_edges) == 2:
            product *= first.id

    return product


def parse(filename: str) -> List[Tile]:
    with open(filename, 'r') as f:
        return [Tile(t) for t in f.read().strip().split('\n\n')]


if __name__ == '__main__':
    tiles = parse('day_20/input.txt')
    print(f'Product of corner tile ids: {part_1(tiles)}')
