from collections import deque
from os import EX_PROTOCOL
from typing import Deque, Tuple


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
    player_1_wins = play_game(player_1, player_2)
    winner = player_1 if player_1_wins else player_2
    return calculate_score(winner)


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
            player_1_wins = play_game(deque(player_1), deque(player_2))
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
