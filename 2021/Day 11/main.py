from ..pull2021 import AocInteraction


#  https://adventofcode.com/2021/day/11

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:

        advent_of_code.answer(1, None)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:

        advent_of_code.answer(2, None)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
