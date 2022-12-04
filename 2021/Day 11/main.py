from pull2021 import AocInteraction


#  https://adventofcode.com/2021/day/11

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        count = 0
        octopuses = []
        for line in input_file:
            octopuses.append([int(x) for x in list(line.strip())])

        for s in range(0, 100):
            step_done = False
            for x in range(0, len(octopuses)):
                for y in range(0, len(octopuses[x])):
                    octopuses[x][y] += 1
            while not step_done:
                step_done = True
                for x in range(0, len(octopuses)):
                    for y in range(0, len(octopuses[x])):
                        if octopuses[x][y] > 9:
                            octopuses[x][y] = -1
                            step_done = False
                            count += 1
                            for i in range(-1, 2):
                                for j in range(-1, 2):
                                    if 0 <= x+i < len(octopuses) and 0 <= y+j < len(octopuses[i]) and octopuses[x+i][y+j] != 0:
                                        octopuses[x+i][y+j] += 1

        advent_of_code.answer(1, count)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        count = 0
        octopuses = []
        for line in input_file:
            octopuses.append([int(x) for x in list(line.strip())])

        all_flash = False
        steps = 0
        while not all_flash:
            steps += 1
            step_done = False
            all_flash = True
            for x in range(0, len(octopuses)):
                for y in range(0, len(octopuses[x])):
                    if octopuses[x][y] != 0:
                        all_flash = False
                    octopuses[x][y] += 1
            while not step_done:
                step_done = True
                for x in range(0, len(octopuses)):
                    for y in range(0, len(octopuses[x])):
                        if octopuses[x][y] > 9:
                            octopuses[x][y] = -1
                            step_done = False
                            count += 1
                            for i in range(-1, 2):
                                for j in range(-1, 2):
                                    if 0 <= x + i < len(octopuses) and 0 <= y + j < len(octopuses[i]) and \
                                            octopuses[x + i][y + j] != 0:
                                        octopuses[x + i][y + j] += 1
        advent_of_code.answer(2, steps-1)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
