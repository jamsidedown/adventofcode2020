from functools import reduce
from operator import or_
import re
from typing import Dict, List, Set


ingredient_pattern = re.compile(r'^([\w\s]+) \(contains ([\w\s,]+)\)$')


class Food:
    def __init__(self, input: str):
        ingredients, allergens = ingredient_pattern.match(input).groups()
        self.ingredients = set(ingredients.split(' '))
        self.allergens = set(allergens.split(', '))

    def __repr__(self) -> str:
        ingredients = ' '.join(self.ingredients)
        allergens = ', '.join(self.allergens)
        return f'Food({ingredients} (contains {allergens}))'


def part_1(foods: List[Food]) -> int:
    all_ingredients = reduce(or_, [food.ingredients for food in foods])
    allergens = get_allergens(foods)
    non_allergens = all_ingredients - set(allergens.values())

    return sum(sum(non_allergen in food.ingredients for food in foods) for non_allergen in non_allergens)


def part_2(foods: List[Food]) -> str:
    allergens = get_allergens(foods)
    return ','.join(allergens[allergen] for allergen in sorted(allergens))


def get_allergens(foods: List[Food]) -> Dict[str, str]:
    all_allergens = reduce(or_, [food.allergens for food in foods])

    allergens_dict: Dict[str, Set[str]] = {}
    for allergen in all_allergens:
        for food in foods:
            if allergen in food.allergens:
                if allergen not in allergens_dict:
                    allergens_dict[allergen] = set(food.ingredients)
                else:
                    allergens_dict[allergen] &= food.ingredients

    correct_allergens = {}
    while allergens_dict:
        for allergen in allergens_dict:
            if len(allergens_dict[allergen]) == 1:
                value = next(iter(allergens_dict.pop(allergen)))
                correct_allergens[allergen] = value
                for allergen_set in allergens_dict.values():
                    allergen_set -= {value}
                break

    return correct_allergens


def parse(filename: str) -> List[Food]:
    with open(filename, 'r') as f:
        return [Food(line) for line in f if line]


if __name__ == '__main__':
    foods = parse('day_21/input.txt')
    print(f'Non-allergen appearences: {part_1(foods)}')
    print(f'Dangerous ingredients: {part_2(foods)}')
