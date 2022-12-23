from pull import AocInteraction


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 10000000 + self.y


#  https://adventofcode.com/2022/day/15

def part_1(advent_of_code, file_as_string_array):
    coll = []
    for line in file_as_string_array:
        line.replace(":", "").replace("x=", "").replace("y=", "").replace(",", "")

    advent_of_code.answer(1, None)


def part_2(advent_of_code, file_as_string_array):
    advent_of_code.answer(2, None)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
