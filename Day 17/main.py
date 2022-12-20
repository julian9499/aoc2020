from pull import AocInteraction


#  https://adventofcode.com/2022/day/17

def part_1(advent_of_code, file_as_string_array):
    
    advent_of_code.answer(1, None)


def part_2(advent_of_code, file_as_string_array):
    
    advent_of_code.answer(2, None)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
