from pull import AocInteraction


#  https://adventofcode.com/2021/day/3

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        count = 0
        for line in input_file:
            index = 0
            count += 1
            for i in range(0, len(line)):
                if line[i] == "1":
                    gamma[index] += 1
                index += 1
        finalg = ""
        finale = ""
        for g in gamma:
            if g > (count / 2):
                finalg += "1"
                finale += "0"
            else:
                finalg += "0"
                finale += "1"

        gammaInt = int(finalg, 2)
        epsilon = int(finale, 2)

        advent_of_code.answer(1, gammaInt * epsilon)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        input = []
        for line in input_file:
            input.append(line.replace("\n", ""))

        oxygen = input.copy()
        co2 = input.copy()

        removeOxy = []
        removeCo2 = []

        for i in range(0, 12):
            countOxy = 0
            for oxy in oxygen:
                countOxy += int(oxy[i])
            if countOxy >= (len(oxygen) - countOxy):
                mostCommonOxy = "1"
            else:
                mostCommonOxy = "0"

            countCo2 = 0
            for co in co2:
                countCo2 += int(co[i])
            if countCo2 >= (len(co2) - countCo2):
                leastCommonCo2 = "0"
            else:
                leastCommonCo2 = "1"

            for oxy in oxygen:
                if oxy[i] != mostCommonOxy and len(oxygen) != 1:
                    removeOxy.append(oxy)
            for co in co2:
                if co[i] != leastCommonCo2 and len(co2) != 1:
                    removeCo2.append(co)

            for o in removeOxy:
                oxygen.remove(o)
            for c in removeCo2:
                co2.remove(c)
            removeOxy = []
            removeCo2 = []
            print(str(mostCommonOxy == leastCommonCo2) + " " + mostCommonOxy)

        print(oxygen[0])
        print(co2[0])
        ansOxy = int(oxygen[0], 2)
        ansCo2 = int(co2[0], 2)
        advent_of_code.answer(2, ansOxy*ansCo2)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
