from pull import AocInteraction


#  https://adventofcode.com/2022/day/1

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        elfs = []
        currElf = []
        for line in input_file:
            if line == "\n":
                elfs.append(currElf)
                currElf = []
            else:
                currElf.append(int(line.strip()))

        highestcount = 0
        for elf in elfs:
            count = 0
            for c in elf:
                count = count + c
            if count > highestcount:
                highestcount = count
            count = 0

        advent_of_code.answer(1, highestcount)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        elfs = []
        currElf = []
        for line in input_file:
            if line == "\n":
                elfs.append(currElf)
                currElf = []
            else:
                currElf.append(int(line.strip()))

        counts = []
        for elf in elfs:
            count = 0
            for c in elf:
                count = count + c
            counts.append(count)
        counts.sort()

        advent_of_code.answer(2, sum(counts[-3:]))


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
