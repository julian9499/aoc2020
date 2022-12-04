from pull2021 import AocInteraction


#  https://adventofcode.com/2021/day/12



def part_1(advent_of_code):
    m = {}

    with open('input.txt', 'r') as input_file:
        for line in input_file:
            n1 = line.strip().split("-")[0]
            n2 = line.strip().split("-")[1]

            if n1 in m.keys():
                m[n1].add(n2)
            else:
                m[n1] = set()
                m[n1].add(n2)
            if n2 in m.keys():
                m[n2].add(n1)
            else:
                m[n2] = set()
                m[n2].add(n1)

        count = traverse(m, set(), "start")


        advent_of_code.answer(1, count)


def traverse(m, visited, current):
    if current == "end":
        return 1
    newVisited = visited.copy()
    if current.islower():
        newVisited.add(current)
    count = 0
    for n in m[current]:
        if n != "start" and n not in visited:
            count += traverse(m, newVisited, n)
    return count




def part_2(advent_of_code):
    m = {}

    with open('input.txt', 'r') as input_file:
        for line in input_file:
            n1 = line.strip().split("-")[0]
            n2 = line.strip().split("-")[1]

            if n1 in m.keys():
                m[n1].add(n2)
            else:
                m[n1] = set()
                m[n1].add(n2)
            if n2 in m.keys():
                m[n2].add(n1)
            else:
                m[n2] = set()
                m[n2].add(n1)


        count = traverse_twice(m, set(), "start", [], False)

        advent_of_code.answer(2, count)

def traverse_twice(m, visited, current, path, stop_lower):
    path.append(current)
    if current == "end":
        return 1
    newVisited = visited.copy()
    new_lower = stop_lower
    if current.islower() and current not in visited:
        newVisited.add(current)
    elif current.islower() and not stop_lower:
        new_lower = True
    count = 0
    for n in m[current]:
        if n != "start" and (n not in visited or (not new_lower and n in visited)):
            count += traverse_twice(m, newVisited, n, path.copy(),new_lower)
    return count


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
