from pull2021 import AocInteraction
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


#  https://adventofcode.com/2021/day/9

def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        m = []
        for line in input_file:
            m.append(list(map(int, list(line.strip()))))
        total = 0
        for i in range(0, len(m)):
            for j in range(0, len(m[i])):
                v = m[i][j]

                if ((i+1 < len(m) and m[i+1][j] > v) or i+1 >= len(m)) and ((i-1 >= 0 and m[i-1][j] > v) or i-1 < 0) and ((j+1 < len(m[i]) and m[i][j+1] > v) or j+1 >= len(m[i])) and ((j-1 >= 0 and m[i][j-1] > v) or j-1 < 0):
                    total += v + 1


        advent_of_code.answer(1, total)


def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        m = []
        visited = []
        x = []
        y = []
        for line in input_file:
            m.append(list(map(int, list(line.strip()))))
            visited.append([False for x in list(map(int, list(line.strip())))])
        total = []
        for i in range(0, len(m)):
            for j in range(0, len(m[i])):
                v = m[i][j]

                if ((i+1 < len(m) and m[i+1][j] > v) or i+1 >= len(m)) and\
                        ((i-1 >= 0 and m[i-1][j] > v) or i-1 < 0) and\
                        ((j+1 < len(m[i]) and m[i][j+1] > v) or j+1 >= len(m[i])) and\
                        ((j-1 >= 0 and m[i][j-1] > v) or j-1 < 0):
                    total.append(travel(m, i, j, visited))
        total.sort()
        print(total)
        largest_basins = total[len(total)-1]
        largest_basins *= total[len(total)-2]
        largest_basins *= total[len(total)-3]


        advent_of_code.answer(2, largest_basins)

def travel(m, i, j, visited):
    v = 1
    visited[i][j] = True

    if i + 1 < len(m) and m[i + 1][j] != 9 and not(visited[i + 1][j]):
        v += travel(m, i+1, j, visited)

    if i - 1 >= 0 and m[i - 1][j] != 9 and not(visited[i - 1][j]):
        v += travel(m, i-1, j, visited)

    if j + 1 < len(m[i]) and m[i][j + 1] != 9 and not(visited[i][j + 1]):
        v += travel(m, i, j + 1, visited)

    if j - 1 >= 0 and m[i][j - 1] != 9 and not(visited[i][j - 1]):
        v += travel(m, i, j - 1, visited)

    return v


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
