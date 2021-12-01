from pull import AocInteraction

def apply_mask(mask, val):
    orMask = int(mask.replace("X", "0"), 2)
    andMask = int(mask.replace("X", "1"), 2)

    return (int(val) & andMask) | orMask


def combinations(string, idx):
    if idx == len(string):
        return [string]

    if string[idx] == "X":
        l1 = combinations(string.replace("X", "1", 1), idx + 1)
        l2 = combinations(string.replace("X", "0", 1), idx + 1)
        # print(l1)
        # print(l2)
        l1.extend(l2)
        return l1
    else:
        l1 = combinations(str(string), idx + 1)
        # print(string + " " + str(idx+1))
        return l1


def apply_mask2(mask, val):
    orMask = int(mask.replace("X", "0"), 2)

    normalVal = bin(int(val) | orMask)[-36:].replace("b", "")

    while len(normalVal) < 36:
        normalVal = "0" + normalVal

    floating = ""
    for m in range(0, len(mask)):
        if mask[m] == "X":
            floating += "X"
        else:
            floating += normalVal[m]


    combs = [int(v,2) for v in combinations(floating, 0)]

    return combs


def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        mem = {}
        instructions = []
        for lines in input_file:
            sep = lines.strip().split(" = ")
            instructions.append((sep[0], sep[1], sep[1]))

        for i in range(0, len(instructions)):
            if "mem" in instructions[i][0]:
                val = instructions[i][0][4:len(instructions[i][0]) - 1]
                instructions[i] = ("mem", val, instructions[i][1])

        mask = instructions[0][2]
        for ins in instructions:
            if ins[0] == "mem":
                mem[ins[1]] = apply_mask(mask, ins[2])
            if ins[0] == "mask":
                mask = ins[2]

        val = sum(mem.values())

        advent_of_code.answer(1, val)

def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        mem = {}
        instructions = []
        for lines in input_file:
            sep = lines.strip().split(" = ")
            instructions.append((sep[0], sep[1], sep[1]))

        for i in range(0, len(instructions)):
            if "mem" in instructions[i][0]:
                val = instructions[i][0][4:len(instructions[i][0]) - 1]
                instructions[i] = ("mem", val, instructions[i][1])

        mask = instructions[0][2]
        for ins in instructions:
            if ins[0] == "mem":
                mems = apply_mask2(mask, ins[1])
                for m in mems:
                    mem[m] = int(ins[2])
            if ins[0] == "mask":
                mask = ins[2]

        val = sum(mem.values())
        advent_of_code.answer(2, val)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
