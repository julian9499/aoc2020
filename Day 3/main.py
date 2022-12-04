from pull import AocInteraction
from functools import reduce


#  https://adventofcode.com/2022/day/3

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        total = 0

        for line in input_file:
            char_list = [*line.strip()]
            split = int(len(char_list)/2)
            compartment_1 = char_list[:split]
            compartment_2 = char_list[-split:]
            highest_prio = 0
            for c in compartment_1:
                if c in compartment_2:
                    if str(c).isupper():
                        highest_prio += ord(c) - 38
                    else:
                        highest_prio += ord(c) - 96
                    break
            total += highest_prio

        advent_of_code.answer(1, total)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        elfs = [set(list(x.strip())) for x in input_file.readlines()]
        total = 0

        for i in range(0, len(elfs), 3):
            c = elfs[i].intersection(elfs[i+1]).intersection(elfs[i+2]).pop()
            if str(c).isupper():
                total += ord(c) - 38
            else:
                total += ord(c) - 96

        advent_of_code.answer(2, total)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
