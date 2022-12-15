from pull import AocInteraction


#  https://adventofcode.com/2022/day/5

def part_1(advent_of_code, file_as_string_array):
    ind = 0
    for i in range(0, len(file_as_string_array)):
        if file_as_string_array[i].strip() == "":
            ind = i

    stacks = []
    for k in range(0, ind):
        stacks.append([])
    for i in range(0, ind-1):
        index = 0
        line = list(file_as_string_array[i].replace("\n", ""))
        for j in range(0, len(stacks)):
            if index+1 < len(line) and line[index+1] != ' ':
                stacks[int(index/4)].append(line[index + 1])
            index += 4
        # [amount, from, to]
    for k in range(0, ind):
        stacks[k].reverse()
    moves = []
    for i in range(ind+1, len(file_as_string_array)):
        amount = int(file_as_string_array[i].strip().split(" ")[1])
        fr = int(file_as_string_array[i].strip().split(" ")[3])
        to = int(file_as_string_array[i].strip().split(" ")[5])
        moves.append([amount, fr, to])

    for m in moves:
        for i in range(0, m[0]):
            p = stacks[m[1]-1].pop()
            stacks[m[2]-1].append(p)

    s = ""
    for i in stacks:
        s += i.pop()

    advent_of_code.answer(1, s)


def part_2(advent_of_code, file_as_string_array):
    ind = 0
    for i in range(0, len(file_as_string_array)):
        if file_as_string_array[i].strip() == "":
            ind = i

    stacks = []
    for k in range(0, ind):
        stacks.append([])
    for i in range(0, ind-1):
        index = 0
        line = list(file_as_string_array[i].replace("\n", ""))
        for j in range(0, len(stacks)):
            if index+1 < len(line) and line[index+1] != ' ':
                stacks[int(index/4)].append(line[index + 1])
            index += 4
        # [amount, from, to]
    moves = []
    for i in range(ind+1, len(file_as_string_array)):
        amount = int(file_as_string_array[i].strip().split(" ")[1])
        fr = int(file_as_string_array[i].strip().split(" ")[3])
        to = int(file_as_string_array[i].strip().split(" ")[5])
        moves.append([amount, fr, to])

    for k in stacks:
        k.reverse()

    for m in moves:
        f = []
        for i in range(0, m[0]):
            p = stacks[m[1]-1].pop()
            f.append(p)
        f.reverse()
        for i in f:
            stacks[m[2]-1].append(i)

    s = ""
    for i in stacks:
        s += i.pop()

    advent_of_code.answer(2, s)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
