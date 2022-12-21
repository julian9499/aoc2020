from pull import AocInteraction


#  https://adventofcode.com/2022/day/21

class Sum:

    def __init__(self, name, v1, operator, v2):
        self.name = name
        self.v1 = v1
        self.operator = operator
        self.v2 = v2

    def setVal(self, m):
        if self.v1 in m and self.v2 in m:
            if self.operator == "+":
                m[self.name] = m[self.v1] + m[self.v2]
            if self.operator == "-":
                m[self.name] = m[self.v1] - m[self.v2]
            if self.operator == "*":
                m[self.name] = m[self.v1] * m[self.v2]
            if self.operator == "/":
                m[self.name] = m[self.v1] / m[self.v2]
            return True
        else:
            return False

def part_1(advent_of_code, file_as_string_array):
    vars = {}
    sums = []
    for line in file_as_string_array:
        splitted = line.replace(":", "").split(" ")
        if len(splitted) == 2:
            vars[splitted[0]] = int(splitted[1])
        else:
            sums.append(Sum(splitted[0], splitted[1], splitted[2], splitted[3]))



    while len(sums) > 0:
        sumsToRemove = []
        for s in sums:
            if s.setVal(vars):
                sumsToRemove.append(s)
        for s in sumsToRemove:
            sums.remove(s)

    print(vars["root"])



    advent_of_code.answer(1, int(vars["root"]))


def part_2(advent_of_code, file_as_string_array):
    vars = {}
    sums = []
    for line in file_as_string_array:
        splitted = line.replace(":", "").split(" ")
        if len(splitted) == 2:
            vars[splitted[0]] = int(splitted[1])
        else:
            vars[splitted[0]] = Sum(splitted[0], splitted[1], splitted[2], splitted[3])
            # sums.append(Sum(splitted[0], splitted[1], splitted[2], splitted[3]))

    sum_string = ""
    start = "root"
    if isinstance(vars["root"], Sum):
        toCheck1 = traverse(vars, vars["root"].v1)
        operator = "="
        toCheck2 = traverse(vars, vars["root"].v2)
        # print(eval(toCheck1))
        print(toCheck1)
        check2 = int(eval(toCheck2))
        x = 1
        eq = False
        while not eq:
            print(int(eval(toCheck1))-check2)

            if check2 == int(eval(toCheck1)):
                eq = True
                print(x)
                advent_of_code.answer(2, x)
                break
            x += int((int(eval(toCheck1))-check2)/ 10) + 1

    print(vars["root"])


def traverse(vars, v):
    if v == "humn":
        return "x"

    if isinstance(vars[v], Sum):
        toCheck1 = traverse(vars, vars[v].v1)
        operator = vars[v].operator
        toCheck2 = traverse(vars, vars[v].v2)
        sum_string = "(" + toCheck1 + operator + toCheck2 + ")"
        return sum_string
    else:
        return str(vars[v])


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    # part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
