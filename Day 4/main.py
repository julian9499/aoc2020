from pull import AocInteraction


#  https://adventofcode.com/2022/day/4

def part_1(advent_of_code, file_as_string_array):
    count = 0
    for line in file_as_string_array:
        elfs = line.split(',')
        elf1 = [int(x) for x in elfs[0].split('-')]
        elf2 = [int(x) for x in elfs[1].split('-')]
        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            count += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            count += 1

    advent_of_code.answer(1, count)


def part_2(advent_of_code, file_as_string_array):
    count = 0
    for line in file_as_string_array:
        elfs = line.split(',')
        elf1 = [int(x) for x in elfs[0].split('-')]
        elf2 = [int(x) for x in elfs[1].split('-')]
        if elf1[0] <= elf2[0] <= elf1[1]:
            count += 1
        elif elf1[0] <= elf2[1] <= elf1[1]:
            count += 1
        elif elf2[0] <= elf1[0] <= elf2[1]:
            count += 1
        elif elf2[0] <= elf1[1] <= elf2[1]:
            count += 1

    advent_of_code.answer(2, count)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
