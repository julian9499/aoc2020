from pull import AocInteraction

class Pos:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 40000000 + self.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.distance})"

    def inDis(self, pos):
        return self.distance >= abs(pos.x-self.x)+abs(pos.y-self.y)

#  https://adventofcode.com/2022/day/15

def part_1(advent_of_code, file_as_string_array):
    sensors = []
    beacons = set()
    lowest_x = 0
    highest_x = 0
    highest_dis = 0

    for line in file_as_string_array:
        line_arr = line.replace(",", "").replace(":", "").replace("=", " ").split(" ")
        x1 = int(line_arr[3])
        y1 = int(line_arr[5])
        x2 = int(line_arr[11])
        y2 = int(line_arr[13])
        highest_x = max(highest_x, max(x1, x2))
        lowest_x = min(lowest_x, min(x1, x2))
        highest_dis = max(highest_dis, abs(x1-x2) + abs(y1-y2))
        sensors.append(Pos(x1, y1, abs(x1-x2) + abs(y1-y2)))
        beacons.add(Pos(x2,y2, 0))

    print(sensors)
    print(highest_x)
    y = 2000000
    count = 0
    for x in range(lowest_x-highest_dis, highest_x+highest_dis):
        for s in sensors:
            if s.distance >= abs(x-s.x)+abs(y-s.y) and Pos(x, y, 0) not in beacons:
                count += 1
                break
    print(count)

    advent_of_code.answer(1, count)


def part_2(advent_of_code, file_as_string_array):
    sensors = []
    beacons = set()
    lowest_x = 0
    highest_x = 0
    highest_dis = 0

    for line in file_as_string_array:
        line_arr = line.replace(",", "").replace(":", "").replace("=", " ").split(" ")
        x1 = int(line_arr[3])
        y1 = int(line_arr[5])
        x2 = int(line_arr[11])
        y2 = int(line_arr[13])
        highest_x = max(highest_x, max(x1, x2))
        lowest_x = min(lowest_x, min(x1, x2))
        highest_dis = max(highest_dis, abs(x1-x2) + abs(y1-y2))
        sensors.append(Pos(x1, y1, abs(x1-x2) + abs(y1-y2)))
        beacons.add(Pos(x2,y2, 0))

    # print(sensors)
    # print(highest_x)
    count = 0
    m = 0
    mx = 4000000
    found_p = Pos(0,0,0)
    checkable_points = set()
    for s in sensors:
        dis = s.distance
        h_y = s.y + dis + 1
        m_y = s.y - dis - 1
        for x in range(0, dis+1):
            posChecks = [Pos(s.x + x, h_y, 0), Pos(s.x - x, h_y, 0), Pos(s.x + x, m_y, 0), Pos(s.x - x, m_y, 0)]
            for p in posChecks:
                if m <= p.x <= mx and m <= p.y <= mx:
                    checkable_points.add(p)
            h_y -= 1
            m_y += 1
        print(len(checkable_points))

    for p in checkable_points:
        collision = False
        for s in sensors:
            collision = collision or s.inDis(p)
            if collision:
                break
        if not collision:
            print(p)
            found_p = p
            break

    print(found_p)


    # for x in range(m, mx):
    #     for y in range(m, mx):
    #         p = Pos(x, y, 0)
    #         collision = False
    #         for s in sensors:
    #             collision = collision or s.inDis(p)
    #             if collision:
    #                 break
    #         if not collision:
    #             print(p)
    #             found_p = p
    #     if x % 400000:
    #         print("10%")

    print(found_p.x * 4000000 + found_p.y)


    advent_of_code.answer(2, found_p.x * 4000000 + found_p.y)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    # part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
