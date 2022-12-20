from pull import AocInteraction

class valve:
    def __init__(self, name, flow_rate, neighbours):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbours = neighbours

    def __repr__(self):
        return f"{self.name} {self.flow_rate} {self.neighbours}"


#  https://adventofcode.com/2022/day/16

def part_1(advent_of_code, file_as_string_array):
    valves = {}
    for line in file_as_string_array:
        name = line.split(" ")[1]
        flow_rate = int(line.split(" ")[4].replace("rate=", "").replace(";", ""))
        neighbours = line.replace(",", "").split(" ")[9:]
        valves[name] = valve(name, flow_rate, neighbours)

    print(valves)
    cache = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(max_flow(set(), 30, 0, valves, "AA",cache))
    advent_of_code.answer(1, None)

def max_flow(visited, min_left, score, valves, curr_location,cache):
    if min_left == 0:
        return score
    elif min_left < 0:
        return cache[0]
    new_score = score + sum([valves[x].flow_rate for x in visited])
    if cache[min_left-1] > new_score:
        return cache[min_left-1]
    else:
        cache[min_left-1] = new_score
    new_vis = visited.copy()
    new_min_left = min_left
    max_val = 0
    if valves[curr_location].flow_rate != 0: #opening valve
        extra_score = score + sum([valves[x].flow_rate for x in visited])
        if cache[min_left-2] <= extra_score:
            cache[min_left-2] = extra_score
            new_vis.add(curr_location)
            new_min_left -= 1
            for n in valves[curr_location].neighbours:
                max_val = max(max_val, max_flow(new_vis, new_min_left - 1, extra_score, valves, n, cache))

    for n in valves[curr_location].neighbours:
        max_val = max(max_val, max_flow(visited, new_min_left - 1, new_score, valves, n, cache))
    print(cache[0])

    return max_val

def part_2(advent_of_code, file_as_string_array):
    
    advent_of_code.answer(2, None)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('test.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
