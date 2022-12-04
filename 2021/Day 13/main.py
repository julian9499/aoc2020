from pull2021 import AocInteraction
import numpy as np


#  https://adventofcode.com/2021/day/13

def part_1(advent_of_code):
    points = []
    folds = []
    with open('test.txt', 'r') as input_file:
        folding_time = False
        for line in input_file:
            if len(line.strip()) == 0:
                folding_time = True
                continue
            if not folding_time:
                points.append([int(x) for x in line.strip().split(",")])
            else:
                l = line.strip().split(" ")[2].split("=")
                folds.append([l[0], int(l[1])])

        for f in folds:
            newPoints = []
            for p in points:
                newP = p.copy()
                if folds[0][0] == "x":
                    if p[0] > f[1]:
                        dis = abs(p[0] - f[1])
                        newP[0] = p[0] - dis
                elif folds[0][0] == "y":
                    if p[1] > f[1]:
                        dis = abs(p[1] - f[1])
                        newP[1] = p[1] - dis
                found = False
                for pi in newPoints:
                    if newP[0] == pi[0] and newP[1] == pi[1]:
                        found = True
                if not found:
                    newPoints.append(newP)
            points = newPoints
        print(points)
        print(len(points))

        advent_of_code.answer(1, None)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:

        advent_of_code.answer(2, None)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
