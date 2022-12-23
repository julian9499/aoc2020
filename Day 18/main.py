from pull import AocInteraction


class Pos:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return self.z * 100000000000 + self.x * 100000 + self.y

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


#  https://adventofcode.com/2022/day/18

def part_1(advent_of_code, file_as_string_array):
    drops = set()

    for line in file_as_string_array:
        coords = [int(x) for x in line.split(',')]
        drops.add(Pos(coords[0], coords[1], coords[2]))

    count = 0
    sides = [
        [0, 0, 1],
        [0, 0, -1],
        [0, 1, 0],
        [0, -1, 0],
        [1, 0, 0],
        [-1, 0, 0],
    ]
    for d in drops:
        for s in sides:
            if Pos(d.x + s[0], d.y + s[1], d.z + s[2]) not in drops:
                count += 1
    print(count)

    # advent_of_code.answer(1, count)


def part_2(advent_of_code, file_as_string_array):
    drops = set()

    for line in file_as_string_array:
        coords = [int(x) for x in line.split(',')]
        drops.add(Pos(coords[0], coords[1], coords[2]))

    count = 0
    sides = [
        [0, 0, 1],
        [0, 0, -1],
        [0, 1, 0],
        [0, -1, 0],
        [1, 0, 0],
        [-1, 0, 0],
    ]

    airdroplets = set()
    for d in drops:
        for s in sides:
            if Pos(d.x + s[0], d.y + s[1], d.z + s[2]) not in drops:
                count += 1
                airdroplets.add(Pos(d.x + s[0], d.y + s[1], d.z + s[2]))

    dropsToIgnore = set()
    for a in airdroplets:
        toVisit = []
        toVisit.append(a)
        visited = set()
        while len(toVisit) > 0:
            currLoc = toVisit.pop()
            if len(visited) > 1000:
                break

            visited.add(currLoc)
            for s in sides:
                addLoc = Pos(currLoc.x + s[0], currLoc.y + s[1], currLoc.z + s[2])
                if addLoc not in drops and addLoc not in visited:
                    toVisit.append(addLoc)
        if len(visited) < 1000:
            dropsToIgnore.add(a)

    print(len(dropsToIgnore))
    print(len(airdroplets))
    print(dropsToIgnore)

    count = 0
    for d in drops:
        for s in sides:
            loc = Pos(d.x + s[0], d.y + s[1], d.z + s[2])
            if loc not in drops and loc not in dropsToIgnore:
                count += 1

    print(count)

    advent_of_code.answer(2, count)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
