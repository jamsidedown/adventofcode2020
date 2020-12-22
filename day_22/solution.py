from collections import deque
from functools import lru_cache
from typing import Deque, Tuple


class HDeque(deque):
    def __hash__(self) -> int:
        return hash(str(self))


def part_1(player_1: Deque[int], player_2: Deque[int]) -> int:
    while player_1 and player_2:
        first = player_1.popleft()
        second = player_2.popleft()
        if first > second:
            player_1.append(first)
            player_1.append(second)
        else:
            player_2.append(second)
            player_2.append(first)

    winner = player_1 if player_1 else player_2
    return calculate_score(winner)


def calculate_score(cards: Deque[int]) -> int:
    length = len(cards)
    return sum(cards.popleft() * (length - i) for i in range(length))


def part_2(player_1: Deque[int], player_2: Deque[int]) -> int:
    p1, p2 = HDeque(player_1), HDeque(player_2)
    player_1_wins = play_game(p1, p2)
    winner = p1 if player_1_wins else p2
    return calculate_score(winner)


@lru_cache
def play_game(player_1: Deque[int], player_2: Deque[int]) -> bool:
    rounds = set()

    while player_1 and player_2:
        round = f'{str(player_1)};{str(player_2)}'
        if round in rounds:
            return True
        rounds.add(round)

        first = player_1.popleft()
        second = player_2.popleft()

        player_1_wins = True

        if len(player_1) >= first and len(player_2) >= second:
            player_1_wins = play_game(HDeque(player_1), HDeque(player_2))
        else:
            player_1_wins = first > second

        if player_1_wins:
            player_1.append(first)
            player_1.append(second)
        else:
            player_2.append(second)
            player_2.append(first)

    return len(player_1) > len(player_2)


def parse(filename: str) -> Tuple[Deque[int], Deque[int]]:
    with open(filename, 'r') as f:
        return (deque(int(card.strip()) for card in deck.splitlines()[1:]) for deck in f.read().split('\n\n'))


if __name__ == '__main__':
    p1, p2 = parse('day_22/input.txt')
    print(f'Winner\'s score: {part_1(p1, p2)}')
    p1, p2 = parse('day_22/input.txt')
    print(f'Winner\'s recursive score: {part_2(p1, p2)}')
