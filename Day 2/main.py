from pull import AocInteraction


#  https://adventofcode.com/2022/day/2

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        totalcount = 0
        for line in input_file:
            chars = line.strip().split(" ")
            opponent = chars[0]
            me = chars[1]

            count = 0
            if me == "X":
                count = count + 1
            if me == "Y":
                count = count + 2
            if me == "Z":
                count = count + 3

            if (me == "X" and opponent == "A") or (me == "Y" and opponent == "B") or (me == "Z" and opponent == "C"):
                count = count + 3
            elif (me == "X" and opponent == "C") or (me == "Y" and opponent == "A") or (me == "Z" and opponent == "B"):
                count = count + 6
            totalcount = totalcount + count
        advent_of_code.answer(1, totalcount)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        totalcount = 0
        for line in input_file:
            chars = line.strip().split(" ")
            opponent = chars[0]
            me = chars[1]

            count = 0
            if me == "X":
                if opponent == "A":
                    count = count + 3
                elif opponent == "B":
                    count = count + 1
                elif opponent == "C":
                    count = count + 2
                count = count + 0
            if me == "Y":
                if opponent == "A":
                    count = count + 1
                elif opponent == "B":
                    count = count + 2
                elif opponent == "C":
                    count = count + 3
                count = count + 3
            if me == "Z":
                if opponent == "A":
                    count = count + 2
                elif opponent == "B":
                    count = count + 3
                elif opponent == "C":
                    count = count + 1
                count = count + 6

            totalcount = totalcount + count
        advent_of_code.answer(2, totalcount)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
