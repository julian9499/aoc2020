from pull2021 import AocInteraction


#  https://adventofcode.com/2021/day/7

def part_1(advent_of_code, file_as_string_array):
    l = [int(x) for x in file_as_string_array[0].split(",")]
    l.sort()

    total = 100000000000
    for i in range(0, len(l)):
        result = sum([abs(l[i] - int(x)) for x in l])
        if result < total:
            total = result

    advent_of_code.answer(1, total)


def part_2(advent_of_code, file_as_string_array):
    l = [int(x) for x in file_as_string_array[0].split(",")]

    total = 100000000000
    m = {}
    for i in range(0, 10000, 10):
        fuel_cost(i, m)
    for i in range(0, len(l)):
        result = sum([fuel_cost(abs(l[i] - int(x)), m) for x in l])
        if result < total:
            total = result

    advent_of_code.answer(2, total)

def fuel_cost(steps,m):
    if steps == 0:
        return 0
    if m.get(steps) is None:
        m[steps] = steps + fuel_cost(steps-1, m)

    return m.get(steps)



if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    f = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, f)
    part_2(aoc_interaction, f)
