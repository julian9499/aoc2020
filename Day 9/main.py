from pull import AocInteraction
import matplotlib.pyplot as plt
import matplotlib.colors
import csv
import numpy as np
import pandas as pd
import seaborn as sns

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x *100000 + self.y


#  https://adventofcode.com/2022/day/9

def part_1(advent_of_code, file_as_string_array):
    visited = {Pos(400, 400)}
    head_visited = {Pos(400, 400)}
    curr_tail_pos = {"x": 400, "y": 400}
    curr_head_pos = {"x": 400, "y": 400}

    for line in file_as_string_array:
        dir = line.split(" ")[0]
        amount = int(line.split(" ")[1])
        # Move head
        for i in range(0, amount):
            if dir == "U":
                curr_head_pos["y"] += 1
            elif dir == "D":
                curr_head_pos["y"] -= 1
            elif dir == "L":
                curr_head_pos["x"] -= 1
            elif dir == "R":
                curr_head_pos["x"] += 1


            if (abs(curr_tail_pos["x"] - curr_head_pos["x"]) > 1 and abs(curr_tail_pos["y"] - curr_head_pos["y"]) == 1) or (abs(curr_tail_pos["x"] - curr_head_pos["x"]) == 1 and abs(curr_tail_pos["y"] - curr_head_pos["y"]) > 1):
                newX = curr_tail_pos["x"]
                newY = curr_tail_pos["y"]
                if curr_tail_pos["x"] < curr_head_pos["x"]:
                    newX += 1
                else:
                    newX -= 1
                if curr_tail_pos["y"] < curr_head_pos["y"]:
                    newY += 1
                else:
                    newY -= 1
                curr_tail_pos["x"] = newX
                curr_tail_pos["y"] = newY
            if abs(curr_tail_pos["x"] - curr_head_pos["x"]) > 1:
                if curr_tail_pos["x"] < curr_head_pos["x"]:
                    curr_tail_pos["x"] += 1
                else:
                    curr_tail_pos["x"] -= 1
            elif abs(curr_tail_pos["y"] - curr_head_pos["y"]) > 1:
                if curr_tail_pos["y"] < curr_head_pos["y"]:
                    curr_tail_pos["y"] += 1
                else:
                    curr_tail_pos["y"] -= 1

            visited.add(Pos(curr_tail_pos["x"], curr_tail_pos["y"]))
    print(len(visited))
    print(len(head_visited))

    df = pd.DataFrame({'x': [x.x for x in visited],
                       'y': [x.y for x in visited],
                       "data": [1.5 for x in visited]})
    dfhead = pd.DataFrame({'x': [x.x for x in head_visited],
                       'y': [x.y for x in head_visited],
                       "data": [1 for x in head_visited]})

    # plot
    sns.scatterplot(data=dfhead, x="x", y="y", s=0.75, alpha=0.5)
    sns.scatterplot(data=df, x="x", y="y", s=0.75, alpha=0.5)
    plt.show()

    advent_of_code.answer(1, len(visited))


def part_2(advent_of_code, file_as_string_array):
    visited = {Pos(0, 0)}
    head_visited = {Pos(0, 0)}
    currPos = []
    for i in range(0, 10):
        currPos.append({"x": 0, "y": 0})
    for line in file_as_string_array:
        dir = line.split(" ")[0]
        amount = int(line.split(" ")[1])
        # Move head
        for _ in range(0, amount):
            if dir == "U":
                currPos[0]["y"] += 1
            elif dir == "D":
                currPos[0]["y"] -= 1
            elif dir == "L":
                currPos[0]["x"] -= 1
            elif dir == "R":
                currPos[0]["x"] += 1

            for i in range(1, 10):
                dx = currPos[i]["x"] - currPos[i-1]["x"]
                dy = currPos[i]["y"] - currPos[i-1]["y"]
                if (abs(dx) > 1 and abs(dy) != 0) or (abs(dx) != 0 and abs(dy) > 1):
                    if dx < 0:
                        currPos[i]["x"] += 1
                    else:
                        currPos[i]["x"] -= 1
                    if dy < 0:
                        currPos[i]["y"] += 1
                    else:
                        currPos[i]["y"] -= 1
                elif abs(dx) > 1:
                    if dx < 0:
                        currPos[i]["x"] += 1
                    else:
                        currPos[i]["x"] -= 1
                elif abs(dy) > 1:
                    if dy < 0:
                        currPos[i]["y"] += 1
                    else:
                        currPos[i]["y"] -= 1
            # print(currPos[9])
            visited.add(Pos(currPos[9]["x"], currPos[9]["y"]))
            head_visited.add(Pos(currPos[0]["x"], currPos[0]["y"]))


    print(len(visited))

    advent_of_code.answer(2, len(visited))


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    # part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
