from typing import Dict, List, Tuple


def part_1(player_1: List[int], player_2: List[int]) -> int:
    while player_1 and player_2:
        first, second = player_1[0], player_2[0]
        player_1, player_2 = player_1[1:], player_2[1:]

        if first > second:
            player_1 += [first, second]
        else:
            player_2 += [second, first]

    winner = player_1 if player_1 else player_2
    return calculate_score(winner)


def calculate_score(cards: List[int]) -> int:
    length = len(cards)
    return sum(cards[i] * (length - i) for i in range(length))


def part_2(player_1: List[int], player_2: List[int]) -> int:
    player_1, player_2, player_1_wins = play_game(player_1, player_2)
    winner = player_1 if player_1_wins else player_2
    return calculate_score(winner)


game_results: Dict[str, bool] = {}

def play_game(player_1: List[int], player_2: List[int]) -> Tuple[List[int], List[int], bool]:
    game = f'{str(player_1)};{str(player_2)}'
    if game in game_results:
        return player_1, player_2, game_results[game]

    rounds = set()
    while player_1 and player_2:
        round = f'{str(player_1)};{str(player_2)}'
        if round in rounds:
            game_results[game] = True
            return player_1, player_2, True
        rounds.add(round)

        first, second = player_1[0], player_2[0]
        player_1, player_2 = player_1[1:], player_2[1:]

        if len(player_1) >= first and len(player_2) >= second:
            _, _, player_1_wins = play_game(player_1[0:first], player_2[0:second])
        else:
            player_1_wins = first > second

        if player_1_wins:
            player_1 += [first, second]
        else:
            player_2 += [second, first]

    player_1_wins = len(player_1) > len(player_2)
    game_results[game] = player_1_wins
    return player_1, player_2, player_1_wins


def parse(filename: str) -> Tuple[List[int], List[int]]:
    with open(filename, 'r') as f:
        return (list(int(card.strip()) for card in deck.splitlines()[1:]) for deck in f.read().split('\n\n'))


if __name__ == '__main__':
    p1, p2 = parse('day_22/input.txt')
    print(f'Winner\'s score: {part_1(p1, p2)}')
    p1, p2 = parse('day_22/input.txt')
    print(f'Winner\'s recursive score: {part_2(p1, p2)}')
