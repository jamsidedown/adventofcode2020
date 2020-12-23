from typing import Dict, Iterator, List


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: 'Node' = None
        self.prev: 'Node' = None

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
            node.prev = current
            if current:
                current.next = node
            else:
                first = node
            current = node
        first.prev = current
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
        current_node = node
        for _ in range(count):
            popped.append(current_node)
            next_node = current_node.next
            prev_node = current_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
            current_node.next = None
            current_node.prev = None
            current_node = next_node
        return popped

    def insert(self, target: Node, nodes: List[Node]) -> None:
        current = target
        next_node = current.next
        for node in nodes:
            node.prev = current
            node.next = next_node
            current.next = node
            next_node.prev = node
            current = node


def part_1(cups: List[int], moves: int) -> str:
    cups = play(cups, moves)
    oi = cups.index(1)
    result = cups[oi + 1:] + cups[0:oi]
    return ''.join(str(x) for x in result)


def play(cups: List[int], moves: int) -> List[int]:
    max_cup = max(cups)
    cll = CLL(cups)
    for mi in range(moves):
        if mi > 0 and mi % 1_000_000 == 0:
            print(f'{mi:_}')
        current = cll.current
        pick_up = cll.pop(current.next, 3)

        destination = (current.value - 1) % max_cup or max_cup
        while destination in {cup.value for cup in pick_up}:
            destination = (destination - 1) % max_cup or max_cup

        dest_node = cll.find(destination)
        cll.insert(dest_node, pick_up)
        cll.next()

    cll.current = cll.find(1)
    return list(cll)


def part_2(cups: List[int], moves: int) -> int:
    max_cup = max(cups)
    cups += list(range(max_cup + 1, 1_000_001))
    cups = play(cups, moves)
    one = cups.index(1)
    return cups[one + 1] * cups[one + 2]


def parse(input: str) -> List[int]:
    return [int(char) for char in input.strip()]


if __name__ == '__main__':
    cups = parse('463528179')
    print(f'Labels on cups after cup 1: {part_1(cups, 100)}')
    print(f'Product of cups with stars: {part_2(cups, 10_000_000)}')
