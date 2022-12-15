from pull import AocInteraction

#  https://adventofcode.com/2022/day/10

def part_1(advent_of_code, file_as_string_array):
    cycles = []
    x = 1

    for line in file_as_string_array:
        if line == "noop":
            cycles.append(x)
        else:
            cycles.append(x)
            cycles.append(x + int(line.split(" ")[1]))
            x = x + int(line.split(" ")[1])

    count = 0

    for i in range(20, 221, 40):
        print(i)
        print(cycles[i-1])
        print(i * cycles[i-2])
        count += i * cycles[i-2]
    print(cycles[218:225])
    print(count)

    advent_of_code.answer(1, count)


def part_2(advent_of_code, file_as_string_array):
    cycles = []
    x = 1
    cycles.append(x)
    # cycles.append(x)

    for line in file_as_string_array:
        if line == "noop":
            cycles.append(x)
        else:
            cycles.append(x)
            cycles.append(x + int(line.split(" ")[1]))
            x = x + int(line.split(" ")[1])

    count = 0

    for i in range(0, 6):
        str =""
        for j in range(0, 40):
            if abs(cycles[i*40+j] - j) <= 1:
                str += "#"
            else:
                str += "."
        print(str)
    advent_of_code.answer(2, "efuglpap")

if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
