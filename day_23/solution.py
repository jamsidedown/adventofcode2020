from typing import Dict, Iterator, List


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: 'Node' = None

    def __repr__(self) -> str:
        return f'Node({self.value})'


class CLL:
    def __init__(self, nodes: List[int]):
        self.lookup: Dict[int, Node] = {}
        first: Node = None
        current: Node = None
        for n in nodes:
            node = Node(n)
            self.lookup[n] = node
            if current:
                current.next = node
            else:
                first = node
            current = node
        current.next = first
        self.current = first

    def __iter__(self) -> Iterator[int]:
        start = self.current
        current = self.current
        yield current.value
        while (current := current.next) != start:
            yield current.value

    def find(self, value: int) -> Node:
        return self.lookup.get(value)

    def next(self):
        self.current = self.current.next

    def pop(self, node: Node, count: int) -> List[Node]:
        popped = []
        start, current = node, node.next
        for _ in range(count):
            popped.append(current)
            current = current.next
        start.next = current
        return popped

    def insert(self, target: Node, nodes: List[Node]) -> None:
        nodes[-1].next = target.next
        target.next = nodes[0]


def part_1(cups: List[int], moves: int) -> str:
    cll = play(cups, moves)
    cll.next()
    icll = iter(cll)
    return ''.join(str(next(icll)) for _ in range(len(cups) - 1))


def play(cups: List[int], moves: int) -> CLL:
    max_cup = max(cups)
    cll = CLL(cups)
    for mi in range(moves):
        if mi > 0 and mi % 1_000_000 == 0:
            print(f'{mi:_}')
        current = cll.current
        pick_up = cll.pop(current, 3)

        destination = (current.value - 1) % max_cup or max_cup
        while destination in {cup.value for cup in pick_up}:
            destination = (destination - 1) % max_cup or max_cup

        dest_node = cll.find(destination)
        cll.insert(dest_node, pick_up)
        cll.next()

    cll.current = cll.find(1)
    return cll


def part_2(cups: List[int], moves: int) -> int:
    max_cup = max(cups)
    cups += list(range(max_cup + 1, 1_000_001))
    cll = play(cups, moves)
    cll.next()
    icll = iter(cll)
    return next(icll) * next(icll)


def parse(input: str) -> List[int]:
    return [int(char) for char in input.strip()]


if __name__ == '__main__':
    cups = parse('463528179')
    print(f'Labels on cups after cup 1: {part_1(cups, 100)}')
    print(f'Product of cups with stars: {part_2(cups, 10_000_000)}')
