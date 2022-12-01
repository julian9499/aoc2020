from pull import AocInteraction


#  https://adventofcode.com/2021/day/2

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        x = 0
        y = 0
        for line in input_file:
            word = line.split(" ")[0]
            steps = int(line.split(" ")[1])
            if word == "forward":
                x += steps
            elif word == "down":
                y += steps
            elif word == "up":
                y -= steps


        advent_of_code.answer(1, x*y)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        aim = 0
        x = 0
        y = 0
        for line in input_file:
            word = line.split(" ")[0]
            steps = int(line.split(" ")[1])
            if word == "forward":
                x += steps
                y += aim * steps
            elif word == "down":
                aim += steps
            elif word == "up":
                aim -= steps

        advent_of_code.answer(2, x*y)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
