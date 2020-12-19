from functools import lru_cache
import re
from typing import Dict, List, Tuple


rule_pattern = re.compile(r'^(\d+): (.*)$')


class Rules:
    def __init__(self, rules: List[str]):
        self.rules: Dict[int, str] = {}
        for line in rules:
            match = rule_pattern.match(line)
            index, rule = match.groups()
            self.rules[int(index)] = rule

    @lru_cache
    def regex(self, index: int, part_2: bool = False) -> str:
        rule = self.rules[index]
        options = []
        for option in rule.split('|'):
            option_pattern = r''
            for part in option.strip().split(' '):
                if part.isnumeric():
                    if int(part) == index:
                        continue
                    else:
                        option_pattern += self.regex(int(part), part_2)
                        if part_2:
                            if index == 8:
                                option_pattern += '+'
                            if index == 11:
                                option_pattern += '{{{n11}}}'
                else:
                    option_pattern += part.replace('"', '').strip()
            options.append(option_pattern)
            if part_2:
                if index == 8 or index == 11:
                    break

        if len(options) > 1:
            pattern = '|'.join(options)
            return f'({pattern})'
        return options[0]

def part_1(input_rules: List[str], messages: List[str]) -> int:
    rules = Rules(input_rules)
    regex = re.compile(f'^{rules.regex(0)}$')
    return sum(bool(regex.match(message)) for message in messages)


def part_2(input_rules: List[str], messages: List[str], depth: int = 5) -> int:
    rule_transform = {'8: 42': '8: 42 | 42 8', '11: 42 31': '11: 42 31 | 42 11 31'}
    input_rules = [rule_transform.get(r, r) for r in input_rules]
    rules = Rules(input_rules)
    regex = rules.regex(0, True)
    regexes = [regex.format(n11=str(i)) for i in range(1, depth)]
    patterns = [re.compile(f'^{r}$') for r in regexes]
    return sum(bool(any(pattern.match(message) for pattern in patterns)) for message in messages)


def parse(filename: str) -> Tuple[List[str], List[str]]:
    with open(filename, 'r') as f:
        rules, messages = f.read().strip().split('\n\n')
        rules = rules.split('\n')
        messages = messages.split('\n')
    return rules, messages


if __name__ == '__main__':
    rules, messages = parse('day_19/input.txt')
    print(f'Number of valid messages: {part_1(rules, messages)}')
    print(f'Number of valid messages (recursive): {part_2(rules, messages)}')
