from pull import AocInteraction


#  https://adventofcode.com/2022/day/14

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rest = False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 100000 + self.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

class line:
    def __init__(self, x1, x2, y1, y2):
        if x1 > x2:
            self.x1 = x2
            self.x2 = x1
        else:
            self.x1 = x1
            self.x2 = x2

        if y1 > y2:
            self.y1 = y2
            self.y2 = y1
        else:
            self.y1 = y1
            self.y2 = y2

    def collision(self, pos):
        if self.y1 <= pos.y <= self.y2 and self.x1 <= pos.x <= self.x2:
            return True
        else:
            return False


def part_1(advent_of_code, file_as_string_array):
    lines = []
    sand_locations = []
    highest_y = 0
    for l in file_as_string_array:
        local_lines = [[int(x) for x in y.split(",")] for y in l.split(" -> ")]
        for i in range(0, len(local_lines) - 1):
            if max(local_lines[i][1],local_lines[i+1][1]) > highest_y:
                highest_y = max(local_lines[i][1],local_lines[i+1][1])
            lines.append(line(local_lines[i][0], local_lines[i+1][0], local_lines[i][1], local_lines[i + 1][1]))
    print(highest_y)
    rest = True
    while rest:
        sand = Pos(500, 0)
        while not sand.rest:
            newPos = Pos(sand.x, sand.y + 1)  # first down
            if newPos.y > highest_y:
                rest = False
                sand.rest = True
                break
            collision = False
            for h in lines:
                collision = collision or h.collision(newPos)
            collision = (newPos in sand_locations) or collision
            if not collision:
                sand = newPos
                continue

            newPos = Pos(sand.x - 1, sand.y + 1)  # down and left
            collision = False
            for h in lines:
                collision = collision or h.collision(newPos)
            collision = (newPos in sand_locations) or collision
            if not collision:
                sand = newPos
                continue

            newPos = Pos(sand.x + 1, sand.y + 1)  # down and right
            collision = False
            for h in lines:
                collision = collision or h.collision(newPos)
            collision = (newPos in sand_locations) or collision
            if not collision:
                sand = newPos
            else:
                sand.rest = True
                sand_locations.append(sand)

    advent_of_code.answer(1, len(sand_locations))


def part_2(advent_of_code, file_as_string_array):
    lines = []
    sand_locations = set()
    highest_y = 0
    for l in file_as_string_array:
        local_lines = [[int(x) for x in y.split(",")] for y in l.split(" -> ")]
        for i in range(0, len(local_lines) - 1):
            if max(local_lines[i][1], local_lines[i + 1][1]) > highest_y:
                highest_y = max(local_lines[i][1], local_lines[i + 1][1])
            lines.append(line(local_lines[i][0], local_lines[i + 1][0], local_lines[i][1], local_lines[i + 1][1]))
    lines.append(line(-10000000, 100000000, highest_y +2, highest_y +2))
    rest = True
    while rest:
        sand = Pos(500, 0)
        print(len(sand_locations))
        while not sand.rest:
            newPos = Pos(sand.x, sand.y + 1)  # first down
            collision = False
            for h in lines:
                collision = collision or h.collision(newPos)
            collision = (newPos in sand_locations) or collision
            if not collision:
                sand = newPos
                continue

            newPos = Pos(sand.x - 1, sand.y + 1)  # down and left
            collision = False
            for h in lines:
                collision = collision or h.collision(newPos)
            collision = (newPos in sand_locations) or collision
            if not collision:
                sand = newPos
                continue

            newPos = Pos(sand.x + 1, sand.y + 1)  # down and right
            collision = False
            for h in lines:
                collision = collision or h.collision(newPos)
            collision = (newPos in sand_locations) or collision
            if not collision:
                sand = newPos
            else:
                sand.rest = True
                sand_locations.add(sand)
                if sand.x == 500 and sand.y == 0:
                    rest = False
                    sand.rest = True
                    break
    print(sand_locations)
    print(len(sand_locations))

    advent_of_code.answer(2, len(sand_locations))


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    # part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
