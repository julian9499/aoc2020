from pull import AocInteraction

class Pos:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Elf:

    def __init__(self, currPos, proposedDir):
        self.currPos = currPos
        self.proposedDir = proposedDir

    def __hash__(self):
        return self.currPos.x *1000000 + self.currPos.y

    def __eq__(self, other):
        self.currPos.x == other.currPos.x and self.currPos.y == other.currPos.y

#  https://adventofcode.com/2022/day/23

def part_1(advent_of_code, file_as_string_array):
    m = []
    elfs = []

    for line in file_as_string_array:
        m.append(line.split())

    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if m[i][j] == "#":
                elfs.append(Elf(Pos(i, j), Pos(-1, -1)))

    for e in elfs:
        hit = False
        for i in range(-1, 2):
            if Pos(e.currPos.x + i, e.currPos.y) in



    advent_of_code.answer(1, None)


def part_2(advent_of_code, file_as_string_array):
    
    advent_of_code.answer(2, None)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
