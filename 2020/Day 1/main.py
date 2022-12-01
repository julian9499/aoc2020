from pull import AocInteraction


#  https://adventofcode.com/2021/day/1

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        numbers = []
        for line in input_file:
            numbers.append(int(line))
        increases = 0
        prev = 0
        for i in range(1, len(numbers)):
            if numbers[i] > numbers[prev]:
                increases += 1
            prev = i
        advent_of_code.answer(1, increases)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        numbers = []
        for line in input_file:
            numbers.append(int(line))
        increases = 0
        prev = 0
        for i in range(2, len(numbers)-2):
            if (numbers[i] + numbers[i+1] + numbers[i+2]) > (numbers[prev] + numbers[prev+1] + numbers[prev+2]):
                increases += 1
            prev = i
        advent_of_code.answer(2, increases)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
