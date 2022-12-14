from pull import AocInteraction


#  https://adventofcode.com/2022/day/8

def part_1(advent_of_code, file_as_string_array):
    grid = []
    for line in file_as_string_array:
        grid.append([int(x) for x in list(line)])

    seen = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if i != 0 and i != len(grid)-1 and j != 0 and j != len(grid[i])-1:
                top = max([x[j] for x in grid[0:i]])
                bottom = max([x[j] for x in grid[i+1:len(grid)]])
                left = max(grid[i][0:j])
                right = max(grid[i][j+1:len(grid[i])])

                if grid[i][j] > min(top, bottom, left, right):
                    seen += 1
            else:
                seen += 1


    # advent_of_code.answer(1, seen)


def part_2(advent_of_code, file_as_string_array):
    grid = []
    for line in file_as_string_array:
        grid.append([int(x) for x in list(line)])

    seen = 0
    coords = []

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if i != 0 and i != len(grid) - 1 and j != 0 and j != len(grid[i]) - 1:
                top = max([x[j] for x in grid[0:i]])
                bottom = max([x[j] for x in grid[i + 1:len(grid)]])
                left = max(grid[i][0:j])
                right = max(grid[i][j + 1:len(grid[i])])

                if grid[i][j] > min(top, bottom, left, right):
                    seen += 1
                    coords.append([i,j])
            else:
                seen += 1
    total_count = 0

    for coord in coords:
        i = coord[0]
        j = coord[1]
        views = []
        top = [x[j] for x in grid[0:i]]
        top.reverse()
        bottom = [x[j] for x in grid[i + 1:len(grid)]]
        left = grid[i][0:j]
        left.reverse()
        right = grid[i][j + 1:len(grid[i])]
        views.append(top)
        views.append(bottom)
        views.append(left)
        views.append(right)

        count = 1
        for v in views:
            i_count = 0
            for k in range(0, len(v)):
                if v[k] < grid[i][j]:
                    i_count += 1
                else:
                    i_count += 1
                    break
            count = count * i_count

        if count > total_count:
            total_count = count

    print(total_count)

    advent_of_code.answer(2, total_count)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    file_as_string_array = [x.strip() for x in open('input.txt', 'r').readlines()]
    part_1(aoc_interaction, file_as_string_array)
    part_2(aoc_interaction, file_as_string_array)
